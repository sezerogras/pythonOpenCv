# canny kenar algoritması
import cv2 as cv
resim=cv.imread("linus.jpg",0)
kenar = cv.Canny(resim,130,150) # burada 130 değeri kenar eşik değeri demek
cv.imshow("Resim",resim)
cv.imshow("kenar",kenar)  # bu şekilde obje üzerinde kenarları tespit etmiş oldum
# şerit takip algoritmasında işe yarar



cv.waitKey(0)