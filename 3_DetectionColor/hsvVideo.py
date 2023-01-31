import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\Smith Fernandes\\Documents\\3 -  pibic\\2- video\\FilmagemDoJogoFutebol\\Jogo 01_MVI_9389.mp4")

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_orange = np.array([5, 50, 50])
    upper_orange = np.array([20, 255, 255])

    maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskOrange = cv2.inRange(hsv, lower_orange, upper_orange)

    result = cv2.bitwise_and(frame, frame, mask=maskOrange)

    cv2.imshow('frame', result)
    cv2.imshow('mask', maskOrange)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#=============== so pra olhar o video na camada HSV

# while True:
#     ret, frame = cap.read()
#
#
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     cv2.imshow('frame', hsv)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()