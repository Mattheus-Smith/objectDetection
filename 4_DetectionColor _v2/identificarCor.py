import numpy as np
import cv2

lower_greenCampo = np.array([20,55,76])
upper_greenCampo = np.array([100,130,255])
#============== mascaras de cores -> usada na funcao draw_by_team
lower_white = np.array([50,15,85])
upper_white = np.array([170,150,200])

lower_black = np.array([0,150,0])
upper_black = np.array([100,255,50])

roi = cv2.imread("campo_s20.png")

# Convert Image to Image HSV
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

maskBlack = cv2.inRange(hsv, lower_black, upper_black)
# maskOrange = cv2.inRange(hsv, lower_orange, upper_orange)

result = cv2.bitwise_and(roi, roi, mask=maskBlack)

cv2.imshow('result', result)
cv2.imshow('entrada', roi)

# identificando jogador Azul
# contours, hierarchy = cv2.findContours(maskBlack,
#                                        cv2.RETR_TREE,
#                                        cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow("teste", roi)
#
cv2.waitKey(0)
cv2.destroyAllWindows()

# for pic, contour in enumerate(contours):
#     area = cv2.contourArea(contour)
#     if (area > 100 and area < 600):
#         img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
#
# # identificando jogador Laranja
# contours, hierarchy = cv2.findContours(maskOrange,
#                                        cv2.RETR_TREE,
#                                        cv2.CHAIN_APPROX_SIMPLE)
#
# for pic, contour in enumerate(contours):
#     area = cv2.contourArea(contour)
#     if (area > 150 and area < 600):
#         img = cv2.rectangle(img, x1y1, x2y2, (0, 128, 255), 2)

