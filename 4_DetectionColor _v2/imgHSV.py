import numpy as np
import cv2

roi = cv2.imread("campo_s20.png")

# Convert Image to Image HSV
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

cv2.imshow('entrada', hsv)

#
cv2.waitKey(0)
cv2.destroyAllWindows()

