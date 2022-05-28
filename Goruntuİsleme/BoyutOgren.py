import cv2

oku =cv2.imread("select.jpg")
(yukseklik,genislik,derinlik)=oku.shape
print("yukseklik: {} genislik: {} deriinlik:{}".format(yukseklik,genislik,derinlik))
cv2.imshow("Resim",oku)


cv2.waitKey(0)