import cv2
import os
import sys
import imutils

im0 =cv2.imread(sys.argv[1],1)
imc = cv2.imread(sys.argv[1],1)
im1 =cv2.imread(sys.argv[2],0)

im0 = imutils.resize(im0, width=500)
img = cv2.cvtColor(im0,cv2.COLOR_BGR2GRAY)
im1 = imutils.resize(im1, width=500)
im1 = cv2.GaussianBlur(im1,(21,21),0)

imD = cv2.absdiff(img,im1)
thr = cv2.threshold(imD,25,255, cv2.THRESH_BINARY)[1]


thr = cv2.dilate(thr, None, iterations=2)
(cnts, _) = cv2.findContours(thr.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
idx = 0
xlist=[]
ylist=[]
for c in cnts:
	if cv2.contourArea(c) < 300:#min area, could be define as arg later
		continue
	(x,y,w,h) = cv2.boundingRect(c)
	cv2.rectangle(im0,(x,y),(x+w,y+h),(255,255,0),1)
	xlist.append(x)
	crop = imc[y:y+h,x:x+w]
	idx+=1
	cv2.imwrite('c'+ str(idx) +'.jpg',crop)
cv2.imshow('mov',im0)
cv2.waitKey(0)
cv2.destroyAllWindows()