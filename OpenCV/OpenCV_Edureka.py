import cv2
import numpy as np 
 
img=cv2.imread('color.jpg')
resized=cv2.resize(img,(int(img.shape[1]/7),int(img.shape[0]/7)))
cv2.imshow('Image',resized)
cv2.waitKey(0)