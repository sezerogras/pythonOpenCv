# x ve y ekseni etrafında döndürme
import cv2 as cv
resim = cv.imread("ben.png")
dikineDondurme =cv.flip(resim,0)
yatayDondurme = cv.flip(resim,1)
tumDondurme = cv.flip(resim,1)

cv.imshow("orijinal",resim)
cv.imshow("Dikine",dikineDondurme)
cv.imshow("yatay",yatayDondurme)
cv.imshow("tumDondurme",tumDondurme)


cv.waitKey(0)

