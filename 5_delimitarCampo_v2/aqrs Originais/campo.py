import cv2
import numpy as np
from shapely.geometry import Point, Polygon

img = cv2.imread("campo_s20.png")

points = np.array([[1,865], [2, 674],   #A1, A2
                [89, 608], [1716, 601], #B1, B2
                [1920, 670], [1920,855]], #C1, C2
               np.int32)

cv2.polylines(img, [points], True, (0,255,0), 2)

cv2.imwrite("./img_campo2.jpg", img)

cv2.waitKey(0)