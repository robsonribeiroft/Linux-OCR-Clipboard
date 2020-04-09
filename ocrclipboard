#!/usr/bin/env python

# Author: Robson Ribeiro

from PIL import Image
import cv2
import pytesseract
import os
import time
import clipboard


# config command line for scrot
filename: str = "{}.png".format(str(round(time.time() * 1000)))
quality: int = 100
command: str = "scrot -s {} -q {}".format(filename, quality)
os.system(command)

# read image
img = cv2.imread("./{}".format(filename))

# preprocess image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imwrite(filename, img_threshold)

# tesseract OCR processing
text_result: str = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

# set text to clipboard
clipboard.copy(text_result)

# config script for command-line
# chmod +x your_filename.py
