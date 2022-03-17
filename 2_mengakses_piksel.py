import cv2

gambar = cv2.imread('image\linus.jpg')
(h,w) = image.shape[:2]

cv2.imshow('Gambar Asli', gambar)

#informasi piksel
(b,g,r) = gambar (0,0)
print("Piksel pada (0,0) - Red : {}, Green : {}, Blue : {}".format(r,g,b))
