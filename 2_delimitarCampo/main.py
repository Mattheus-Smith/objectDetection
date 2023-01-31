import cv2
import numpy as np
from shapely.geometry import Point, Polygon

img = cv2.imread("entrada.png")

# points = np.array([[25, 70], [25, 160],
#                 [110, 200], [200, 160],
#                 [200, 70], [110, 20]],
#                np.int32)

points = np.array([[118, 571], [1485, 768],
                [1916, 569], [862,487]],
               np.int32)

color = [255, 0, 0]   # BLUE
thickness = 2
radius = 2

# x1 = int(x1y1[0])
# y1 = int(x1y1[1])
#
# x2 = int(x2y2[0])
# y2 = int(x2y2[1])
#
# xc = x1 + int((x2 - x1) / 2)
# player_pos = (xc, y2)

court = Polygon(points)



#cv2.polylines(img, [points], True, (0,255,0), 2)

# Draw only players that are within the basketball court

# if Point(player_pos).within(court):
#   cv2.circle(img, player_pos, radius, color, thickness, lineType=8, shift=0)

cv2.imshow("saida", img)

cv2.waitKey(0)