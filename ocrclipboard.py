#!/usr/bin/env python

# Author: Robson Ribeiro

from PIL import Image
import cv2
import pytesseract
import os
import time
import clipboard
import numpy


# get grayscale image
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = numpy.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = numpy.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = numpy.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# get Image from selectable screen area
def get_scrot_image():
    filename = "{}.png".format(str(round(time.time() * 1000)))
    quality = 100
    command = "scrot -s {} -q {}".format(filename, quality)
    os.system(command)
    return filename


def main():
    # read image
    filename = get_scrot_image()
    img = cv2.imread(filename)

    # preprocess image
    img_gray = grayscale(img)
    img_threshold = threshold(img_gray)
    cv2.imwrite(filename, img_threshold)

    # tesseract OCR processing
    text_result = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)

    # set text to clipboard
    clipboard.copy(text_result)

    print(text_result)


if __name__ == '__main__':
    main()
