import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread('campo_A51.jpg')

# Four corners of the 3D court + mid-court circle point in source image
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_src = np.array([[46, 545], [1024, 635], #A, B
                [1950, 523], [845, 503]])  #C, D

# cv2.fillPoly(img_src, [pts_src], 255)
cv2.polylines(img_src, [pts_src], isClosed=True, color=[255, 0, 0], thickness=2)

plt.imshow(img_src)
plt.title('Original')
plt.show()

# # Read destination image.
# img_dst = cv2.imread('campo_futebol2.png')
#
# # Four corners of the court + mid-court circle point in destination image
# # Start top-left corner and go anti-clock wise + mid-court circle point
# # pts_dst = np.array([[544,1056], [1388,1056], #A1, C2
# #                 [1552, 434], [1552, 2], #C1, B2
# #                 [4, 2], [4, 406]])  #B1, A2
#
# pts_dst = np.array([[360,1056], [1200,1056], #A1, C2
#                 [1552, 445], [1549, 2], #C1, B2
#                 [5, 5], [5, 390]])  #B1, A2
#
# cv2.fillPoly(img_dst, [pts_dst], 255)
#
# plt.figure()
# plt.imshow(img_dst)
# #plt.show()
#
# #Calculate Homography
# h, status = cv2.findHomography(pts_src, pts_dst)
#
# img_src = cv2.imread('campo_s20.png')
# # Warp source image to destination based on homography
# img_out = cv2.warpPerspective(img_src, h, (img_src.shape[1], img_src.shape[0]),flags=cv2.INTER_LINEAR)
# # cv2.imshow("Warped", img_out)
# # cv2.waitKey(0)
# #
# cv2.imwrite("output.jpg", img_out)