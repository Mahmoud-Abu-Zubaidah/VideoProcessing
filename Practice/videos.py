import cv2
import numpy as np

haarcascade_car = '..\\data\\car.xml'

haarcascade_car = cv2.CascadeClassifier(haarcascade_car)

cap = cv2.VideoCapture('..\\data\\cars.mp4')

counter = 0
while cap.isOpened():
    counter +=1
    
    if counter % 20 ==  0:
        
        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        cars = haarcascade_car.detectMultiScale(gray,2,2)
        
        for (x,y,w,h) in cars:
            
            
            cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255),5)
            
            cv2.putText(frame, 'Car', (x,y-5), cv2.FONT_ITALIC, 0.7, (255,100,0)) 
        
        
        cv2.imshow('Truffic', frame)
        
    if cv2.waitKey(0) == ord('n'):
        continue
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()