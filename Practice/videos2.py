import cv2
import numpy as np

cap = cv2.VideoCapture('..\\data\\A Lemon.mp4')

# we will identify 3 windows
cv2.namedWindow('Input')

cv2.namedWindow('Output')

cv2.namedWindow('Hue channel')
cv2.waitKey(0)
cv2.destroyAllWindows()

while cap.isOpened():
    
    ret, frame = cap.read()
    
    #Just for close when ends
    if ret == False:
        break
    
    #convert frames to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    h = hsv[:,:,0]
    
    #apply threshold
    copy = h.copy()
    
    h[copy > 40] = 0
    h[copy <= 40] = 1
    
    
    
    cv2.imshow('Input', frame)
    # cv2.resizeWindow('Input', 700,700)
    
    cv2.imshow('Output', frame * h[:,:,np.newaxis])
    # cv2.resizeWindow('Output', 700,700)
    
    cv2.imshow('hue', h*255)
    # cv2.resizeWindow('hue', 700,700)
    
    
    if cv2.waitKey(0) == ord('n'):
        continue
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    