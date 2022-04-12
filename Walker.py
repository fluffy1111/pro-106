import cv2

img = cv2.imread("haarcascade_fullbody.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
print(bodies)

for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)