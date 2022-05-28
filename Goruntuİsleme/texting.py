import cv2 as cv

yazdir = cv.imread("iha son .png")
resim=cv.putText(yazdir,"merhaba ben sezer bu da benim İHA'm ",(10,100),cv.FONT_ITALIC,1,(0,250,0),3,None,None)

cv.imshow("pencere",yazdir)
cv.waitKey(0)