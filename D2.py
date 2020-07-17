import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)
 
 # Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
 
while(True):
ret, frame = cap.read()
 
 
 
 
 cv2.imshow('frame',frame)
 if cv2.waitKey(1) & 0xFF == ord('q'):
 break
 else:
 break
 
 # Release everything if job is finished
 cap.release()
 out.release()
 cv2.destroyAllWindows()
