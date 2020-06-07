# pylint --generate-rcfile > .pylintrc
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt


# Import the image
img = cv2.imread('popeye.jpg')

# Convert the image into RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert the image into gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Blurring the image
figure_size = 12 # Dimension of the x and y axis of the karnel
img_blur = cv2.blur(img,(figure_size, figure_size))

# Write the images
cv2.imwrite('popeye_rgb.jpg', img_rgb)
cv2.imwrite('popeye_gray.jpg', img_gray)
cv2.imwrite('popeye_blur.jpg', img_blur)

# Showing the windows
cv2.imshow('Gray Image', img_gray)
cv2.imshow('RGB Image', img_rgb)
cv2.imshow('Blur Image', img_blur)

while(True):
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cv2.destroyAllWindows()