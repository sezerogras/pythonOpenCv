import cv2 as cv

resim123=cv.imread("select.jpg")
(mavi,yesil,kirmizi)=resim123[155,100] # ilk deger y eksseni ikinci deger x ekseni
print("kırmızı degeri : {} yesil degeri: {} mavi degeri : {}".format(kirmizi,yesil,mavi))


