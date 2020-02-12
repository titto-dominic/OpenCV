import cv2
cap=cv2.VideoCapture('Megamind.avi')
print(cap.get(cv2.CAP_PROP_FOURCC))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,360)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
#res = cv2.resize(cap, (1208,720), interpolation=cv2.INTER_LINEAR)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret is True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Frame',gray)
        if cv2.waitKey(1)==ord('q'):
            out=cv2.VideoWriter('megamind_copy.avi',fourcc,20.0,(720,528))
            out.write(frame)
            out.release()
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()