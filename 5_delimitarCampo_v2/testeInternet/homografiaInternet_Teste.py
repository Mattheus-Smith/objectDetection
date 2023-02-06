import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread("campo_s20.png")
# Four corners of the 3D court + mid-court circle point in source image
# Start top-left corner and go anti-clock wise + mid-court circle point
#poligno da imagem q forma um campo em 2d
pts_src = np.array([[1,865], [1920,855],   #A1, C2
                [1920, 670], [1716, 601], #C1, B2
                [89, 608], [2, 674]]) #B1, A2
# cv2.fillPoly(img_src, [pts_src], 255)
cv2.polylines(img_src, [pts_src], isClosed=True, color=[255, 0, 0], thickness=2)

plt.imshow(img_src)
plt.title('Original')
plt.show()

# Read destination image.
img_dst = cv2.imread('imgInternetCourt2D.png')

# Four corners of the court + mid-court circle point in destination image 
# Start top-left corner and go anti-clock wise + mid-court circle point

#poligno da imagem q forma um campo em 2d
pts_dst = np.array([[20,261], [520,261],   #A1, C2
                [540, 200], [540, 0], #C1, B2
                [0, 0], [0, 200]]) #B1, A2

variacao_C1C2 = abs(pts_src[0][0] - pts_src[1][0])
variacao_B1B2 = abs(pts_src[3][0] - pts_src[4][0])
maxVar = max(int(variacao_C1C2), int(variacao_B1B2))

print(variacao_C1C2)
print(variacao_B1B2)

pts_dst = np.array([[40,261], [int(variacao_B1B2)-60,261],   #A1, C2
                [int(variacao_B1B2), 200], [int(variacao_B1B2), 0], #C1, B2
                [0, 0], [0, 200]]) #B1, A2



cv2.fillPoly(img_dst, [pts_dst], 255)

plt.figure()
plt.imshow(img_dst)
plt.show()

# # Calculate Homography
# h, status = cv2.findHomography(pts_src, pts_dst)
#
# # Warp source image to destination based on homography
# img_src2 = cv2.imread('images/3DBasketballMiddleView.jpg')
# img_out = cv2.warpPerspective(img_src2, h, (img_dst.shape[1], img_dst.shape[0]))
# cv2.imshow("Warped", img_out)
# cv2.waitKey(0)
#
# cv2.imwrite("output/middleViewResult.jpg", img_out)