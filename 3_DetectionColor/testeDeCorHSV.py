import numpy as np
import cv2



brg_color = np.float32([[[255, 0, 0]]])

hsv = cv2.cvtColor(brg_color, cv2.COLOR_BGR2HSV)

print(hsv[0])
