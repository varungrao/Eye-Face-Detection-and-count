import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("eye.xml")

#smile_cascade = cv2.CascadeClassifier("smile.xml")

cap = cv2.VideoCapture(0)

while True:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    count=0
    
    for (x,y,w,h) in faces:
          cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
           roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            count=count+1
            eyes = eye_cascade.detectMultiScale(roi_gray)
             for (ex, ey, ew, eh) in eyes:
                  cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
   cv2.imshow('img', img)
   k = cv2.waitKey(30) & 0xff
   if k == 27:
    print("COUNT=",count)
        break
    
cap.release()
cv2.destroyAllWindows()

firebase = firebase.FirebaseApplication('https://iot-ia3-70e74.firebaseio.com/')
data = {'faces': count}
result=firebase.put('https://iot-ia3-70e74.firebaseio.com/','/faces',data)
