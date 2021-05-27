import cv2
import numpy as np
import time

def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.uint8(ycbcr)

if __name__ == '__main__':
 img = cv2.imread('RGB.jpg')
 YCbCr = rgb2ycbcr(img)
 cv2.imwrite("YCbCr_cara_lain.jpg", YCbCr)
 # cv2.imshow("yuhu",YCbCr)
 # cv2.waitKey(0)
