#!/usr/bin/env python

# Author: Robson Ribeiro

from preprocessing import *
from img_io import *

from PIL import Image
import cv2
import pytesseract
import clipboard
import numpy


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
    remove_file(filename)

    # set text to clipboard
    clipboard.copy(text_result)

    print(text_result)


if __name__ == '__main__':
    main()
