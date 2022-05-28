# negatif görüntüye nasıl ulaşılır ona bakacağız
# negatif yapmak aslında görselin tersini almak anlamına geliyor
import cv2 as cv

resim = cv.imread("linus.jpg")
negatif=cv.bitwise_not(resim)
cv.imshow("resim",resim)
cv.imshow("negatif",negatif)
cv.waitKey(0)