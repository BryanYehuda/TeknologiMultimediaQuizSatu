#import library
import cv2

#Membuka gambar
image = cv2.imread('RGB.jpg')

#Mengubah mode BGR ke RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Melakukan convert RGB ke YCbCr
ycbcr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2YCrCb)

#Memisahkan Y, Cb, Cr
Y, Cr, Cb = cv2.split(ycbcr_image)

#Menyimpan file Y, Cb, Cr
cv2.imwrite('Y.jpg',Y)
cv2.imwrite('Cr.jpg',Cr)
cv2.imwrite('Cb.jpg',Cb)

#Menyatukan gambar
img = cv2.merge((Y,Cr,Cb))
cv2.imwrite ('merge_YCbCr.jpg',img)