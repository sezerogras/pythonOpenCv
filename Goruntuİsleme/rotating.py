import cv2 as cv
# bir görüntüyü kendi etrafında döndrme işlemi

resim = cv.imread("renk.jpg")
genislik = 500
yukseklik = 500
merkezNokta = (genislik/2,yukseklik/2)
d = cv.getRotationMatrix2D(merkezNokta,30,1.0)
dondurme=cv.warpAffine(resim,d,(genislik,yukseklik))
cv.imshow("dondurme",dondurme)
cv.imshow("orijinal",resim)



cv.waitKey(0)