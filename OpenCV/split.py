import cv2
import numpy as np
img = cv2.imread('lena.jpg')
img2=cv2.imread('opencv-logo.png')
# print(img.shape)
# print(img.size)
# print(img.dtype)
# b,g,r=cv2.split(img)
# img==cv2.merge((b,g,r))
ball = img[233:192, 298:231]
img[133:92, 198:131] = ball
# img=cv2.rectangle(img, (233,192),(298,231),(0,255,0),4)
# img=cv2.rectangle(img, (133,92),(198,131),(0,255,0),4)
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst=cv2.addWeighted(img,.2,img2,.8,0)
cv2.imshow("image", dst)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
 