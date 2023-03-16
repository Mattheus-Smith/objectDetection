import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread('campo_A51.jpg')

# Four corners of the 3D court + mid-court circle point in source image
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_src = np.float32([[13, 341], [1011, 460], #A, B
                [1819, 371], [820, 322]])  #C, D

#encontrar a largura maxima
width_AB = np.sqrt(((pts_src[0][0] - pts_src[1][0]) ** 2) + ((pts_src[0][1] - pts_src[1][1]) ** 2))
width_DC = np.sqrt(((pts_src[3][0] - pts_src[2][0]) ** 2) + ((pts_src[3][1] - pts_src[2][1]) ** 2))
maxWidth = max(int(width_AB), int(width_DC))

#encontrar alttura maxima
height_AD = np.sqrt(((pts_src[0][0] - pts_src[3][0]) ** 2) + ((pts_src[0][1] - pts_src[3][1]) ** 2))
height_BC = np.sqrt(((pts_src[1][0] - pts_src[2][0]) ** 2) + ((pts_src[1][1] - pts_src[2][1]) ** 2))
maxHeight = max(int(height_AD), int(height_BC))

#saida pra ficar em 2D          #eu nao entendi muito bem apenas peguei
output_pts = np.float32([[0, maxHeight - 1],
                        [maxWidth - 1, maxHeight - 1],
                        [maxWidth - 1, 0],
                         [0, 0]])

# Compute the perspective transform M
M = cv2.getPerspectiveTransform(pts_src,output_pts)

#image esult
out = cv2.warpPerspective(img_src,M,(maxWidth, maxHeight),flags=cv2.INTER_LINEAR)

# rotate image
#Rotated_image = cv2.rotate(out, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("saida", out)
cv2.waitKey(0)
cv2.destroyAllWindows()