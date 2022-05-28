import cv2 as cv
video =cv.VideoCapture("video.mp4")
while True:
    kontrol, yakala = video.read()
    if not kontrol:
        print("video okuma işlemi başarısız!")
    cv.imshow("Goruntu",yakala)
    if cv.waitKey(20) & 0xFF==ord('p'):
        break
