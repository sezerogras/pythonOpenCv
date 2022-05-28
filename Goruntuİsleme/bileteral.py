# bu filtre görüüntünün gürültüsünü szaltır yumuşaklığını arttırır
import cv2 as cv

resim= cv.imread("linus.jpg")
bileteral = cv.bilateralFilter(resim,15,93,43)

cv.imshow("resim",resim)
cv.imshow("bileteral",bileteral)


cv.waitKey(0)