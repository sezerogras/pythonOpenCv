import cv2

resim = cv2.imread("iha son .png")
print(resim)
cv2.imshow("Resim",resim)

cv2.waitKey(2000)