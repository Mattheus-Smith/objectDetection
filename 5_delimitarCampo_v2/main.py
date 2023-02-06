import cv2
import numpy as np
from shapely.geometry import Point, Polygon

img = cv2.imread("campo_s20.png")

points = np.array([[1, 864], [1919, 858], #A1, C2
                [1919, 658], [1716, 591], #C1, B2
                [88, 595], [1, 635]], np.int32)  #B1, A2

cv2.polylines(img, [points], True, (0,255,0), 2)

cv2.imwrite("./img_campo.jpg", img)

cv2.waitKey(0)