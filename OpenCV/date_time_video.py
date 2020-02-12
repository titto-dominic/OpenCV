import cv2
import datetime
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
        font=cv2.FONT_HERSHEY_SIMPLEX
        datet=str(datetime.datetime.now())
        text='WIDTH : '+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+' '+'HEIGHT : '+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame=cv2.putText(frame,datet,(10,75),font,1,(123,223,223),1,cv2.LINE_AA)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1)==ord('q'):
            out=cv2.VideoWriter('megamind_copy.avi',fourcc,20.0,(720,528))
            out.write(frame)
            out.release()
            break
    else:
        break
cap.release()
 
cv2.destroyAllWindows()