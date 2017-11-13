# Learn OpenCV Week 1 - Assignment
#
# Cropping and Refitting


import cv2
import numpy as np

# Reading the image
target = cv2.imread("../../../data/images/sample.jpg",1)

source = cv2.imread("../../../data/images/rose_test.jpg",1)

cv2.imshow('Source',source)
cv2.imshow('Target',target)

print(target.shape)
print(source.shape)

target[100:400,100:400,:] = source[100:400,100:400,:]
cv2.imshow('Transformed',target)

cv2.waitKey(0)
cv2.destroyAllWindows()