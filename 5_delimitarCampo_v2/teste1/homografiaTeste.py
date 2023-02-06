#https://theailearner.com/tag/cv2-warpperspective/

import cv2
import numpy as np

#entrada da imagem
img = cv2.imread("campo_s20.png")

#poligno da imagem q forma um campo em 2d
points = np.array([[1,865], [1920,855],   #A1, C2
                [1920, 670], [1716, 601], #C1, B2
                [89, 608], [2, 674]]) #B1, A2

variacao_C1C2 = abs(points[0][0] - points[1][0])
variacao_B1B2 = abs(points[3][0] - points[4][0])
maxVar = max(int(variacao_C1C2), int(variacao_B1B2))

print(variacao_C1C2)
print(variacao_B1B2)

variacao_C1C2 = 3000


# #saida pra ficar em 2D          #eu nao entendi muito bem apenas peguei
output_pts = np.array([[40,961], [1800,961],   #A1, C2
                [1919, 900], [1919, 0], #C1, B2
                [0, 0], [0, 900]]) #B1, A2
# output_pts = np.float32([[0,0],[0, maxHeight-maxHeightBaixa],
#                         [maxWidth-minWidth-variacao_C1C2, 0],[minWidth+height_A1A2, 0],
#                         [maxWidth - 1, maxHeight-maxHeightBaixa],[maxWidth - 1, 0]])

# Compute the perspective transform M
H, status = cv2.findHomography(points, output_pts)

img_dst = cv2.imread('imgInternetCourt2D.png')
print((img.shape[1], img.shape[0]))
#image esult
# Warp source image to destination based on homography
img_out = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))


# cv2.imshow("Warped", img_out)
# cv2.waitKey(0)
cv2.imwrite("teste.jpg", img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
