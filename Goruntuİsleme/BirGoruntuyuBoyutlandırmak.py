import cv2

resim =cv2.imread("select.jpg")
boyut=(800,800)
boyutlandirilmisHal=cv2.resize(resim,boyut)
cv2.imshow("Orijinal",resim)
cv2.imshow("son hali",boyutlandirilmisHal)
cv2.waitKey(0)
