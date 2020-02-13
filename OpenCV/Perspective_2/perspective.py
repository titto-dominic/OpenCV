import cv2
import numpy as np 
img=cv2.imread('test.jpg')
img=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
img_copy=img

pts=[(0,0),(0,0),(0,0),(0,0)]
pointIndex=0
def draw_circle(event,x,y,flags,param):
	global img
	global pointIndex
	global pts
	
    
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img_copy,(x,y),0,(0,0,250),5)
		pts[pointIndex] = (x,y)
		pointIndex = pointIndex + 1

# cv2.circle(img, (189,84), 5, (0, 0, 255), -1)
# cv2.circle(img, (593,81), 5, (0, 0, 255), -1)
# cv2.circle(img, (17,449), 5, (0, 0, 255), -1)
# cv2.circle(img, (775,449), 5, (0, 0, 255), -1)

def selectFourPoints():
	global img
	global pointIndex
	
	while(pointIndex != 4):
		cv2.imshow('image',img_copy)
		key = cv2.waitKey(20) & 0xFF
		if key == 27:
			return False
	return True

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)


while(1):
	if(selectFourPoints()):
		pts1 = np.float32([[pts[0][0],pts[0][1]],[pts[1][0],pts[1][1]],[pts[2][0],pts[2][1]],[pts[3][0],pts[3][1]]])
		c1=(pts[2][1]-pts[0][1])*2
		c2=(pts[1][0]-pts[0][0])*2
		print(c1,c2)
		ASPECT_RATIO = (c1,c2)
		pts2 = np.float32([[0,0],[ASPECT_RATIO[1],0],[0,ASPECT_RATIO[0]],[ASPECT_RATIO[1],ASPECT_RATIO[0]]])
		M = cv2.getPerspectiveTransform(pts1,pts2)

		while(1):
			dst = cv2.warpPerspective(img,M,(c2,c1))
			cv2.imshow("output",dst)

			key = cv2.waitKey(10) & 0xFF
			if key == 27:
				break
	else:
		print ("Exit")
	break
cv2.imwrite("Perspective_transformed.jpg",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()