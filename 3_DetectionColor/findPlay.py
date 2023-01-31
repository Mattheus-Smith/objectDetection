# Importing the libraries OpenCV and numpy
import cv2
import numpy as np
  
# Read the images
img = cv2.imread("C:\\Users\\Public\\teste1.jpg")
  
# Resizing the image
#image = cv2.resize(img, (200, 300))
  
# Convert Image to Image HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
# Defining lower and upper bound HSV values
lower = np.array([90, 50, 50])
upper = np.array([130, 255, 255])
  
# Defining mask for detecting color
mask = cv2.inRange(hsv, lower, upper)

contours, hierarchy = cv2.findContours(mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(img, (x, y),
                                   (x + w, y + h),
                                   (255, 0, 0), 2)
        cv2.putText(imageFrame, "Blue Colour", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (255, 0, 0))


# Display Image and Mask
cv2.imshow("Image", img)
cv2.imshow("Mask", mask)
  
# Make python sleep for unlimited time
cv2.waitKey(0)