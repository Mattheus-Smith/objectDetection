from absl import logging
import numpy as np
import tensorflow as tf
import cv2

import argparse
import ntpath
from os import walk
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

from yolov3_tf2.funçãoExtra import *

YOLOV3_LAYER_LIST = [
    'yolo_darknet',
    'yolo_conv_0',
    'yolo_output_0',
    'yolo_conv_1',
    'yolo_output_1',
    'yolo_conv_2',
    'yolo_output_2',
]

YOLOV3_TINY_LAYER_LIST = [
    'yolo_darknet',
    'yolo_conv_0',
    'yolo_output_0',
    'yolo_conv_1',
    'yolo_output_1',
]

def load_darknet_weights(model, weights_file, tiny=False):
    wf = open(weights_file, 'rb')
    major, minor, revision, seen, _ = np.fromfile(wf, dtype=np.int32, count=5)

    if tiny:
        layers = YOLOV3_TINY_LAYER_LIST
    else:
        layers = YOLOV3_LAYER_LIST

    for layer_name in layers:
        sub_model = model.get_layer(layer_name)
        for i, layer in enumerate(sub_model.layers):
            if not layer.name.startswith('conv2d'):
                continue
            batch_norm = None
            if i + 1 < len(sub_model.layers) and \
                    sub_model.layers[i + 1].name.startswith('batch_norm'):
                batch_norm = sub_model.layers[i + 1]

            logging.info("{}/{} {}".format(
                sub_model.name, layer.name, 'bn' if batch_norm else 'bias'))

            filters = layer.filters
            size = layer.kernel_size[0]
            in_dim = layer.get_input_shape_at(0)[-1]

            if batch_norm is None:
                conv_bias = np.fromfile(wf, dtype=np.float32, count=filters)
            else:
                # darknet [beta, gamma, mean, variance]
                bn_weights = np.fromfile(
                    wf, dtype=np.float32, count=4 * filters)
                # tf [gamma, beta, mean, variance]
                bn_weights = bn_weights.reshape((4, filters))[[1, 0, 2, 3]]

            # darknet shape (out_dim, in_dim, height, width)
            conv_shape = (filters, in_dim, size, size)
            conv_weights = np.fromfile(
                wf, dtype=np.float32, count=np.product(conv_shape))
            # tf shape (height, width, in_dim, out_dim)
            conv_weights = conv_weights.reshape(
                conv_shape).transpose([2, 3, 1, 0])

            if batch_norm is None:
                layer.set_weights([conv_weights, conv_bias])
            else:
                layer.set_weights([conv_weights])
                batch_norm.set_weights(bn_weights)

    assert len(wf.read()) == 0, 'failed to read all data'
    wf.close()

def broadcast_iou(box_1, box_2):
    # box_1: (..., (x1, y1, x2, y2))
    # box_2: (N, (x1, y1, x2, y2))

    # broadcast boxes
    box_1 = tf.expand_dims(box_1, -2)
    box_2 = tf.expand_dims(box_2, 0)
    # new_shape: (..., N, (x1, y1, x2, y2))
    new_shape = tf.broadcast_dynamic_shape(tf.shape(box_1), tf.shape(box_2))
    box_1 = tf.broadcast_to(box_1, new_shape)
    box_2 = tf.broadcast_to(box_2, new_shape)

    int_w = tf.maximum(tf.minimum(box_1[..., 2], box_2[..., 2]) -
                       tf.maximum(box_1[..., 0], box_2[..., 0]), 0)
    int_h = tf.maximum(tf.minimum(box_1[..., 3], box_2[..., 3]) -
                       tf.maximum(box_1[..., 1], box_2[..., 1]), 0)
    int_area = int_w * int_h
    box_1_area = (box_1[..., 2] - box_1[..., 0]) * \
        (box_1[..., 3] - box_1[..., 1])
    box_2_area = (box_2[..., 2] - box_2[..., 0]) * \
        (box_2[..., 3] - box_2[..., 1])
    return int_area / (box_1_area + box_2_area - int_area)

def draw_outputs_default(img, outputs, class_names):
    boxes, objectness, classes, nums = outputs
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    wh = np.flip(img.shape[0:2])
    for i in range(nums):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        img = cv2.putText(img, '{} {:.4f}'.format(
            class_names[int(classes[i])], objectness[i]),
            x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
    return img

def draw_outputs_by_team(img, outputs, class_names):
    boxes, objectness, classes, nums = outputs
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    wh = np.flip(img.shape[0:2])
    for i in range(nums):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        if (class_names[int(classes[i])] == "person"):

            roi = img[x1y1[1]: x2y2[1], x1y1[0]: x2y2[0]]

            # Convert Image to Image HSV
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
            maskOrange = cv2.inRange(hsv, lower_orange, upper_orange)

            # if (i==2):
            # cv2.imwrite("C:\\Users\\Public\\teste2.jpg", roi)

            # saida = "C:\\Users\\Public\\saida" + str(i) + ".jpg"
            # cv2.imwrite(saida, roi)

            # identificando jogador Azul
            contours, hierarchy = cv2.findContours(maskBlue,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 100 and area < 600):
                    img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)

            # identificando jogador Laranja
            contours, hierarchy = cv2.findContours(maskOrange,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 150 and area < 600):
                    img = cv2.rectangle(img, x1y1, x2y2, (0, 128, 255), 2)

            # img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        # else:
        #     img = cv2.rectangle(img, x1y1, x2y2, (0, 255, 0), 2)
        #
        # img = cv2.putText(img, '{} {:.4f}'.format(
        #     class_names[int(classes[i])], objectness[i]),
        #     x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    return img

def draw_outputs_foot(img, outputs, class_names):
    boxes, objectness, classes, nums = outputs
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    wh = np.flip(img.shape[0:2])
    for i in range(nums):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))

        if (class_names[int(classes[i])] == "person"):

            player_pos = posicao_dos_pes_do_jogador(x1y1,x2y2)        #descobre qual é a posicao dos pes do jogador

            if Point(player_pos).within(court):
                cv2.circle(img, player_pos, radius, color, thickness, lineType=8, shift=0)

    return img

def draw_outputs_by_team_inside_field(img, outputs, class_names):
    boxes, objectness, classes, nums = outputs
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    wh = np.flip(img.shape[0:2])
    for i in range(nums):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))

        if (class_names[int(classes[i])] == "person"):
            roi = img[x1y1[1]: x2y2[1], x1y1[0]: x2y2[0]]
            #cv2.imwrite("./jogador.jpg", roi)

            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

            roi = roi.reshape((roi.shape[0] * roi.shape[1], 3))  # represent as row*column,channel number
            clt = KMeans(n_clusters=3)  # cluster number
            clt.fit(roi)

            hist = find_histogram(clt); #print_colors(hist, clt.cluster_centers_)

            arrayColors = []; array_por_Colors = []
            bar = plot_colors(hist, clt.cluster_centers_, arrayColors, array_por_Colors); #save_color_bar(bar)

            #print(arrayColors); print(array_por_Colors)

            saida = detectionJogador(arrayColors, array_por_Colors); #print(saida)    ####bem aqui eu descubro qual é o jogador (azul ou laranja)

            player_pos = posicao_dos_pes_do_jogador(x1y1, x2y2)  # descobre qual é a posicao dos pes do jogador

            if Point(player_pos).within(court) and saida == 1: #se o jogador esta dentro do campo e for do time azul -> pintar seu pés de azul(colorA)
                cv2.circle(img, player_pos, radius, colorA, thickness, lineType=8, shift=0)

            if Point(player_pos).within(court) and saida == 2: #se o jogador esta dentro do campo e for do time laranja -> pintar seu pés de laranja(colorB)
                cv2.circle(img, player_pos, radius, colorB, thickness, lineType=8, shift=0)

        # img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        # img = cv2.putText(img, '{} {:.4f}'.format(
        #     class_names[int(classes[i])], objectness[i]),
        #     x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
    return img

def seletor_de_funcoes(img, outputs, class_names, opcao):
    if(opcao == 0): #usar funcao draw_outputs_default
        return draw_outputs_default(img, outputs, class_names)
    if (opcao == 1):  # usar funcao draw_outputs_by_team
        return draw_outputs_by_team(img, outputs, class_names)
    if (opcao == 2):  # usar funcao draw_outputs_foot
        return draw_outputs_foot(img, outputs, class_names)
    if (opcao == 3):  # usar funcao draw_outputs_by_team_inside_field
        return draw_outputs_by_team_inside_field(img, outputs, class_names)

def draw_labels(x, y, class_names):
    img = x.numpy()
    boxes, classes = tf.split(y, (4, 1), axis=-1)
    classes = classes[..., 0]
    wh = np.flip(img.shape[0:2])
    for i in range(len(boxes)):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        img = cv2.putText(img, class_names[classes[i]],
                          x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                          1, (0, 0, 255), 2)
    return img


def freeze_all(model, frozen=True):
    model.trainable = not frozen
    if isinstance(model, tf.keras.Model):
        for l in model.layers:
            freeze_all(l, frozen)
