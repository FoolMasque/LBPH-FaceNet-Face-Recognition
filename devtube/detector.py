import cv2
#import numpy as np

face_cascade =cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_alt_tree.xml')

img = cv2.imread('./images/1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=2)

for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Face Detector',img)
cv2.waitKey(0)
cv2.destroyAllWindows()