import cv2
import numpy as np
from shapely.geometry import Point, Polygon

img = cv2.imread("entrada.png")

points = np.array([[118, 571], [1485, 768],
                [1916, 569], [862,487]],
               np.int32)

cv2.polylines(img, [points], True, (0,255,0), 2)

cv2.imwrite("./img_campo.jpg", img)

cv2.waitKey(0)