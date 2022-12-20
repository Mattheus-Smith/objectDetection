import numpy as np
import cv2
from shapely.geometry import Point, Polygon

#============== mascaras de cores -> usada na funcao draw_by_team
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

lower_orange = np.array([5, 50, 50])
upper_orange = np.array([20, 255, 255])

#============== variaveis usadas na funcao draw_foot
points = np.array([[118, 571], [1485, 768],
                [1916, 569], [862,487]],
               np.int32)

color = [255, 0, 255]   # MAGENTA
colorA = [255, 0, 0]   # AZUL
colorB = [0, 79, 242]   # LARANJA
thickness = 2
radius = 2

court = Polygon(points)                                   #criar o campo

def posicao_dos_pes_do_jogador(x1y1, x2y2):
    x1 = int(x1y1[0])
    y1 = int(x1y1[1])

    x2 = int(x2y2[0])
    y2 = int(x2y2[1])

    xc = x1 + int((x2 - x1) / 2)

    return xc, y2

#============== funções extras usadas na draw_outputs_by_team_inside_field

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids, arrayColors, array_por_Colors):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        #print("Color %s" %color.astype("uint8").tolist())
        #print("Percentage %d%%" %int(percent*100))
        arrayColors.append(color.astype("uint8").tolist())
        array_por_Colors.append(int(percent*100))
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

def print_colors(hist, centroids):
    for (percent, color) in zip(hist, centroids):
        p = int(percent*100)
        print("%d%% Color %s" %(p, color))

def save_color_bar(bar):
    #head, tail = ntpath.split(filename)
    #parts = tail.split(".")
    #output = "{}/{}-colorbar.jpg".format(head, parts[0])
    #print("Color bar stored in %s" %output)
    cv2.imwrite("./colobar.jpg", bar)

def detectionJogador(arrayColors, array_por_Colors):
    azul=0
    laranja=0
    for i in range(0,len(arrayColors)):
        cor = cv2.cvtColor(np.uint8([[arrayColors[i]]]), cv2.COLOR_RGB2HSV)
        #print(cor[0][0])
        #print('{0} >= {1} and {2} <= {3}' .format(cor[0][0][0], lower_blue[0], cor[0][0][0],upper_blue[0]))
        if (int(cor[0][0][0]) >= lower_blue[0] and int(cor[0][0][0]) <= upper_blue[0] and int(cor[0][0][1]) > 10):
            azul = 1  # tem azul
            posA = i
        if (int(cor[0][0][0]) >= lower_orange[0] and int(cor[0][0][0]) <= upper_orange[0] and int(cor[0][0][1]) > 10):
            laranja = 1  # tem laranja
            posL = i

    if (azul == 1 and laranja == 1):

        if (array_por_Colors[posA] > array_por_Colors[posL]):
            return 1  # azul
        if (array_por_Colors[posL] > array_por_Colors[posA]):
            return 2  # laranja

    elif (azul == 1 and laranja == 0):
        return 1  # azul
    elif (azul == 0 and laranja == 1):
        return 2  # laranja
    else:
        return 0  # nada

