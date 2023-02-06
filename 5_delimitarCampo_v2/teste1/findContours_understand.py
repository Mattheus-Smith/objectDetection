import cv2
import numpy as np

imagem = cv2.imread("entrada.png", cv2.IMREAD_UNCHANGED)
################################################
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(imagem, imagem, mask=maskBlue)
#'''
imagem_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
#############################################################
thresh, imagem_edges = cv2.threshold(imagem_gray, 40, 255, cv2.THRESH_BINARY)

canvas = np.zeros(result.shape, np.uint8)
canvas.fill(255)
mask = np.zeros(result.shape, np.uint8)
mask.fill(255)

contours_draw, hierachy = cv2.findContours(imagem_edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours_mask, hierachy = cv2.findContours(imagem_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(enumerate(contours_draw))

for contour in range(len(contours_draw)):
    cv2.drawContours(canvas, contours_draw, contour, (0,0,0), 3)
    #cv2.waitKey(0)
    #cv2.imshow("no for", canvas)
#'''
# cv2.imshow("saida", canvas)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()