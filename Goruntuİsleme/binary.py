import cv2 as cv

# bir görüntüyü binary e dönüştürmek istiyorsan ilk önce griye dönüştürmen lazım
resim = cv.imread("renk.jpg",0) # 0 yazdım ve otomatik olarak gri rengine dönüşmüş oldu
kontrol,binary =cv.threshold(resim,150,255,cv.THRESH_BINARY)
kontrol,binary2 =cv.threshold(resim,150,255,cv.THRESH_BINARY_INV)
cv.imshow("binary1 ",binary)
cv.imshow("binary 2",binary2)



cv.waitKey(0)