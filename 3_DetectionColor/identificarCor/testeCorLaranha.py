import numpy as np
import cv2

#============== mascaras de cores -> usada na funcao draw_by_team
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

lower_orange = np.array([5, 50, 50])
upper_orange = np.array([20, 255, 255])

roi = cv2.imread("wpp.jpeg")

hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
maskOrange = cv2.inRange(hsv, lower_orange, upper_orange)

result = cv2.bitwise_and(roi, roi, mask=maskOrange)

cv2.imshow('frame', result)
cv2.imshow('mask', maskOrange)

cv2.waitKey(0)

cv2.destroyAllWindows()