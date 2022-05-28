import cv2 as cv
# resimi bulanıklaştırdım
resim = cv.imread("linus.jpg")
bulanik = cv.GaussianBlur(resim,(11,11),6) # burada sıfır yazılan yere ya sıfır ya da pozitif bir saı yazmalısın aksi taktirdde hata alırsın
# burada dikkat etmen bir diğer nokta çekirdek boyutlarını çift vermezsin (8,8) yazar isen hata alırsın dikkat et
cv.imshow("resim",resim)
cv.imshow("gauss",bulanik)
cv.waitKey(0)