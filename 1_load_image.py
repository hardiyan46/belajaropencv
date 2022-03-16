import cv2

#lokasi gambar
filepath = 'image\linux.png'
image = cv2.imread(filepath)

#show image
cv2.imshow("Gambar Linux", image)
cv2.waitKey(0)

#save image
output = 'image\linux_saveas.png'
cv2.imwrite(output, image)
print("Gambar telah disimpan di {}".format(output))