
"""
Solution of task1 for video processing

np.__version__
Out[20]: '1.26.2'

cv2.__version__
Out[21]: '4.5.5'
"""
import cv2
import numpy as np

fullBody = '..\\data\\haarcascade_fullbody.xml'

fullBody = cv2.CascadeClassifier(fullBody)

cap = cv2.VideoCapture('..\\data\\walking.avi')

while cap.isOpened():
    
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    person = fullBody.detectMultiScale(gray,1.3,2)
    
    for (x,y,w,h) in person:
        
        
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,10,200),3)
        
        cv2.putText(frame, 'Person', (x-15,y-5), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (255,10,0)) 
    
    
    cv2.imshow('People', frame)
    
    if cv2.waitKey(0) == ord('n'):
        continue
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()

