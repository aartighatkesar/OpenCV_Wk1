# Learn OpenCV Week 1 - Assignment
#
# Fun with Thresholding, Simple Segmentation


import cv2
import numpy as np

# Read an image in grayscale
src = cv2.imread("../../../data/images/hillary_clinton.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original1',src)

# Set threshold and maximum value
thresh = 160
maxValue = 255

# Binary threshold
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

cv2.imshow("Thresholded Image1", dst);



# Simple Segmentation
# Read an image in grayscale
src = cv2.imread("../../../data/images/ducks_seg.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original2',src)

dst = np.zeros_like(src)
dst[np.logical_and(src >0,src <30)] =255


cv2.imshow("Thresholded Image2", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()