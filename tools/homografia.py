#https://theailearner.com/tag/cv2-warpperspective/

import cv2
import numpy as np

#entrada da imagem
img = cv2.imread("output.jpg")

#poligno da imagem q forma um campo em 2d
points = np.array([[118, 571], [1485, 768],
                [1916, 569], [862,487]],
               np.float32)

#encontrar a largura maxima
width_AD = np.sqrt(((points[0][0] - points[3][0]) ** 2) + ((points[0][1] - points[3][1]) ** 2))
width_BC = np.sqrt(((points[1][0] - points[2][0]) ** 2) + ((points[1][1] - points[2][1]) ** 2))
maxWidth = max(int(width_AD), int(width_BC))

#encontrar alttura maxima
height_AB = np.sqrt(((points[0][0] - points[1][0]) ** 2) + ((points[0][1] - points[1][1]) ** 2))
height_CD = np.sqrt(((points[2][0] - points[3][0]) ** 2) + ((points[2][1] - points[3][1]) ** 2))
maxHeight = max(int(height_AB), int(height_CD))

#saida pra ficar em 2D          #eu nao entendi muito bem apenas peguei
output_pts = np.float32([[0, 0],
                        [0, maxHeight - 1],
                        [maxWidth - 1, maxHeight - 1],
                        [maxWidth - 1, 0]])

# Compute the perspective transform M
M = cv2.getPerspectiveTransform(points,output_pts)

#image esult
out = cv2.warpPerspective(img,M,(maxWidth, maxHeight),flags=cv2.INTER_LINEAR)

#rotate image
Rotated_image = cv2.rotate(out, cv2.ROTATE_90_COUNTERCLOCKWISE)

#range de cores em RGB
lower_red = np.array([150, 50, 50])
upper_red = np.array([160, 255, 255])

#aplicando mascara pra encontrar a com especifica
hsv = cv2.cvtColor(Rotated_image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_red, upper_red)     # Create a mask with range
result = cv2.bitwise_and(Rotated_image, Rotated_image, mask = mask)   # Performing bitwise and operation with mask in img variable

#mask = cv2.inRange(result, lower_red, upper_red)                       #testar essa mascara

#get all non zero values
coord = cv2.findNonZero(mask)

# Radius of circle
radius = 3

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

court_img = cv2.imread('./campo_futebol.jpg')
for pos in coord:
  center_coordinates = (pos[0][0], pos[0][1])
  cv2.circle(court_img, center_coordinates, radius, color, thickness)

#cv2.imshow("saida", court_img)

#cv2.imshow("saida", mask)
cv2.imwrite("./minimap.jpg", court_img)
#
cv2.waitKey(0)

# h, status = cv2.findHomography(points, points)
# img_out = cv2.warpPerspective(img, h, (points.shape[1], img_dst.shape[0]))
