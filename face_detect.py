import cv2

img=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('C:\\Users\\abine\\Desktop\\py_projects\\haarcascade_frontalface_default.xml')
while True:
    read_ok,frame=img.read()
    g_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_rect=cascade.detectMultiScale(g_img)
    for(x,y,w,h) in face_rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Detected Faces',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows