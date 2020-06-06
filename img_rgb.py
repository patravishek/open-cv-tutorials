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

# Write the images
cv2.imwrite('popeye_rgb.jpg', img_rgb)
cv2.imwrite('popeye_gray.jpg', img_gray)