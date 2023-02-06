#https://theailearner.com/tag/cv2-warpperspective/

import cv2
import numpy as np

#entrada da imagem
img = cv2.imread("campo_s20.png")

#poligno da imagem q forma um campo em 2d
points = np.array([[89, 608], [2, 674],   #B1, A2
                [1,865], [1920,855], #A1, C2
                [1920, 670], [1716, 601]],np.float32) #C1, B2

#encontrar a largura maxima
width_B1B2 = np.sqrt(((points[0][0] - points[5][0]) ** 2) + ((points[0][1] - points[5][1]) ** 2))
maxWidth = width_B1B2

#encontrar a largura debaixo
width_A1C2 = np.sqrt(((points[2][0] - points[3][0]) ** 2) + ((points[2][1] - points[3][1]) ** 2))
minWidth = width_A1C2

#encontrar distancia das alturas baixas
distance_A1A2 = np.sqrt(((points[2][0] - points[1][0]) ** 2) + ((points[2][1] - points[1][1]) ** 2))
distance_C1C2 = np.sqrt(((points[4][0] - points[3][0]) ** 2) + ((points[4][1] - points[3][1]) ** 2))

#variacao em X
variacao_A1A2 = (points[2][0] - points[1][0]) ** 2
variacao_C1C2 = (points[3][1] - points[4][1]) ** 2

#encontrar alttura baixa maxima
height_A1A2= np.sqrt(((distance_A1A2) ** 2) - (variacao_A1A2))
height_C1C2= np.sqrt(((distance_C1C2) ** 2) - (variacao_C1C2))
maxHeightBaixa = max(int(height_A1A2), int(height_C1C2))

#encontrar alttura alta maxima
height_A2B1 = np.sqrt(((points[1][0] - points[0][0]) ** 2) + ((points[1][1] - points[0][1]) ** 2))
height_C1B2 = np.sqrt(((points[4][0] - points[3][0]) ** 2) + ((points[4][1] - points[3][1]) ** 2))
maxHeightAlta = max(int(height_A2B1), int(height_C1B2))
maxHeight = maxHeightBaixa + maxHeightAlta

print(maxHeight, maxWidth)

#saida pra ficar em 2D          #eu nao entendi muito bem apenas peguei
output_pts = np.float32([[0,0],[0, 200],
                        [100, maxHeight-1],[1400, maxHeight-1],
                        [maxWidth - 1, 200],[maxWidth - 1, 0]])

# #saida pra ficar em 2D          #eu nao entendi muito bem apenas peguei
# output_pts = np.float32([[0,0],[0, maxHeight-maxHeightBaixa],
#                         [maxWidth-minWidth-variacao_C1C2, 0],[minWidth+height_A1A2, 0],
#                         [maxWidth - 1, maxHeight-maxHeightBaixa],[maxWidth - 1, 0]])

# Compute the perspective transform M
M = cv2.getPerspectiveTransform(points,output_pts)
#M, status = cv2.findHomography(points, output_pts)

#image esult
out = cv2.warpPerspective(img,M,(int(maxWidth)), int(maxHeight),flags=cv2.INTER_LINEAR)

# rotate image
#Rotated_image = cv2.rotate(out, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("saida", out)

'''

# range de cores em RGB
lower_red = np.array([150, 50, 50])
upper_red = np.array([160, 255, 255])

# aplicando mascara pra encontrar a com especifica
hsv = cv2.cvtColor(Rotated_image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_red, upper_red)  # Create a mask with range
result = cv2.bitwise_and(Rotated_image, Rotated_image,
                         mask=mask)  # Performing bitwise and operation with mask in img variable

# mask = cv2.inRange(result, lower_red, upper_red)                       #testar essa mascara

# get all non zero values
coord = cv2.findNonZero(mask)

# Radius of circle
radius = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 1

court_img = cv2.imread('./campo_futebol.jpg')
for pos in coord:
    center_coordinates = (pos[0][0], pos[0][1])
    cv2.circle(court_img, center_coordinates, radius, color, thickness)

# cv2.imshow("saida", court_img)

# cv2.imshow("saida", mask)
cv2.imwrite("./minimap2.jpg", court_img)

# #poligno da imagem q forma um campo em 2d
# points = np.array([[1,865], [2, 674],   #A1, A2
#                 [89, 608], [1716, 601], #B1, B2
#                 [1920, 670], [1920,855]]) #C1, C2

#encontrar a largura maxima
width_B1B2 = np.sqrt(((points[2][0] - points[3][0]) ** 2) + ((points[2][1] - points[3][1]) ** 2))
width_A1C2 = np.sqrt(((points[0][0] - points[5][0]) ** 2) + ((points[0][1] - points[5][1]) ** 2))
maxWidth = max(int(width_B1B2), int(width_A1C2))

#encontrar alttura baixa maxima
height_A1A2 = np.sqrt(((points[0][0] - points[1][0]) ** 2) + ((points[0][1] - points[1][1]) ** 2))
height_C1C2 = np.sqrt(((points[4][0] - points[5][0]) ** 2) + ((points[4][1] - points[5][1]) ** 2))
maxHeightBaixa = max(int(height_A1A2), int(height_C1C2))

#encontrar alttura alta maxima
height_A2B1 = np.sqrt(((points[1][0] - points[2][0]) ** 2) + ((points[1][1] - points[2][1]) ** 2))
height_C1B2 = np.sqrt(((points[4][0] - points[3][0]) ** 2) + ((points[4][1] - points[3][1]) ** 2))
maxHeightAlta = max(int(height_A2B1), int(height_C1B2))
maxHeight = maxHeightBaixa + maxHeightAlta

#saida pra ficar em 2D          #eu nao entendi muito bem apenas peguei
output_pts = np.float32([[200, 0],[0, 60],
                        [maxWidth - 1, 0],[maxWidth - 1, maxHeight - 1],
                        [maxWidth - 1, 60],[maxWidth - 200, 0]])

'''

cv2.waitKey(0)
cv2.destroyAllWindows()

# h, status = cv2.findHomography(points, points)
# img_out = cv2.warpPerspective(img, h, (points.shape[1], img_dst.shape[0]))
