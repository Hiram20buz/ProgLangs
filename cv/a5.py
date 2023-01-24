import cv2
arc=input("Dame una foto ")
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

img=cv2.imread(arc)
cv2.imshow("x",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    

cv2.imwrite("outputface.jpg",img)
cv2.imshow("y",img)

#dsize=(500,500)
#output=cv2.resize(img,dsize)
#output1=cv2.resize(edges,dsize)
#cv2.imshow("Original",output)
#cv2.imshow("Filtro",output1)
cv2.waitKey(0)
cv2.destroyAllWindows()
