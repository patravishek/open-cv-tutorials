# pylint --generate-rcfile > .pylintrc
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageFilter:
    def __init__(self):
        self.img = cv2.imread('popeye.jpg')

    def convert_rgb(self):
        img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        return img_rgb

    def convert_gray(self):
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return img_gray
    
    def convert_hsv(self):
        img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        return img_hsv

    def convert_blur(self):
        figure_size = 12 # Dimension of the x and y axis of the karnel
        img_blur = cv2.blur(self.img,(figure_size, figure_size))
        return img_blur

def main():
    img = ImageFilter()

    # Write the images
    cv2.imwrite('popeye_rgb.jpg', img.convert_rgb())
    cv2.imwrite('popeye_gray.jpg', img.convert_gray())
    cv2.imwrite('popeye_blur.jpg', img.convert_blur())

    # Showing the windows
    cv2.imshow('Gray Image', img.convert_gray())
    cv2.imshow('RGB Image', img.convert_rgb())
    cv2.imshow('Blur Image', img.convert_blur())

    while(True):
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    
    return()

if __name__== '__main__':
    main()
    cv2.destroyAllWindows()