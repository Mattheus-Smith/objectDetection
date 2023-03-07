import cv2
import numpy as np

# carrega a imagem
image  = cv2.imread("campo_A51.png")

# conversão para o espaço de cores HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# criação da máscara para os pixels pretos
# lower_black = np.array([0, 0, 0])
# upper_black = np.array([180, 255, 50])

lower_black = np.array([5, 50, 50])
upper_black = np.array([12, 255, 255])

mask = cv2.inRange(hsv, lower_black, upper_black)

# aplicação de uma transformação morfológica para remover pequenos objetos e preencher buracos
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# aplicação da máscara na imagem original
result = cv2.bitwise_and(image, image, mask=mask)

# exibe a imagem filtrada
cv2.imshow('Imagem filtrada', result)
cv2.waitKey(0)
cv2.destroyAllWindows()