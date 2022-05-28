import cv2

resim=cv2.imread("select.jpg")
kirpma=resim[60:360,20:380] # ilkiinde başlangıç y ekseni ile sondaki y ekseni ,ikinic durum x için gecerli
cv2.imshow("orijinal",resim)
cv2.imshow("son hali",kirpma)
cv2.waitKey(0) # bu şekilde ben bir  tuşa basana kadar ekranda kalıyor
