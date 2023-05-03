import cv2
import numpy as np

# carrega a imagem
image  = cv2.imread("2imgCampoDrone.jpg")

# conversão para o espaço de cores HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# criação da máscara para os pixels pretos
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])
mask = cv2.inRange(hsv, lower_black, upper_black)

# lower_laranja = np.array([5, 50, 50])
# upper_laranja = np.array([25, 255, 255])
# mask = cv2.inRange(hsv, lower_laranja, upper_laranja)

# lower_green = np.array([40, 50, 50])
# upper_green = np.array([70, 255, 255])
# mask = cv2.inRange(hsv, lower_green, upper_green)


# aplicação de uma transformação morfológica para remover pequenos objetos e preencher buracos
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))             #img drone -> 36, 36
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# aplicação da máscara na imagem original
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imwrite("imagemFiltrada.png", result)

# exibe a imagem filtrada
# cv2.imshow('Imagem filtrada', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()