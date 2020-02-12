import cv2
import numpy as np 
img=cv2.imread('sheet.jpg')
# img=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.circle(img, (189,84), 5, (0, 0, 255), -1)
cv2.circle(img, (593,81), 5, (0, 0, 255), -1)
cv2.circle(img, (17,449), 5, (0, 0, 255), -1)
cv2.circle(img, (775,449), 5, (0, 0, 255), -1)


pts1 = np.float32([[189,81],[593,81],[17,449],[775,449]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
result=cv2.warpPerspective(img,matrix,(500,600))

cv2.imshow('Frame',img)
cv2.imshow("Perspective transformation", result)
cv2.imwrite("perspective_transformed.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()