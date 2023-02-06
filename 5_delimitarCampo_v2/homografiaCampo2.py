import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread('campo_s20.png')

points = np.array([[1, 864], [1919, 858], #A1, C2
                [1919, 658], [1716, 591], #C1, B2
                [88, 595], [1, 635]], np.float32)  #B1, A2

#encontrar a largura maxima
width_B1B2 = np.sqrt(((points[4][0] - points[3][0]) ** 2) + ((points[4][1] - points[3][1]) ** 2))
width_A1C2 = np.sqrt(((points[0][0] - points[1][0]) ** 2) + ((points[0][1] - points[1][1]) ** 2))
maxWidth = max(int(width_B1B2), int(width_A1C2))
print(maxWidth)

#encontrar alttura maxima
height_A1B1 = np.sqrt(((points[4][0] - points[0][0]) ** 2) + ((points[4][1] - points[0][1]) ** 2))
height_C2B2 = np.sqrt(((points[3][0] - points[1][0]) ** 2) + ((points[3][1] - points[1][1]) ** 2))
maxHeight = max(int(height_A1B1), int(height_C2B2))
print(maxHeight)

height_C1B2 = int(np.sqrt(((points[3][0] - points[2][0]) ** 2) + ((points[3][1] - points[2][1]) ** 2)))
height_B1A2 = int(np.sqrt(((points[5][0] - points[4][0]) ** 2) + ((points[5][1] - points[4][1]) ** 2)))
print(height_C1B2)
print(height_B1A2)

pts_dst = np.array([[450,maxHeight], [maxWidth-250,maxHeight], #A1, C2
                [maxWidth, height_C1B2], [maxWidth, 0], #C1, B2
                [0, 0], [0, height_B1A2]], np.float32)  #B1, A2

#Calculate Homography
M, status = cv2.findHomography(points, pts_dst)
#M = cv2.getPerspectiveTransform(pts_src,pts_dst)
# Warp source image to destination based on homography
img_out = cv2.warpPerspective(img_src, M, (maxWidth, maxHeight),flags=cv2.INTER_LINEAR)
# cv2.imshow("Warped", img_out)
# cv2.waitKey(0)
#
cv2.imwrite("output.jpg", img_out)