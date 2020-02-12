import cv2
import numpy as np
#img=np.zeros([512,512,3],np.uint8)
img = cv2.imread("lena.jpg",1)
img=cv2.line(img,(0,0),(255,255),(0,0,255),10)
img=cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),10)
img=cv2.rectangle(img,(380,0),(510,210),(0,255,0),4)
img=cv2.circle(img,(400,200),60,(0,255,0),5)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'TITTO',(10,500),font,4,(100,246,256),4,cv2.LINE_AA)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()