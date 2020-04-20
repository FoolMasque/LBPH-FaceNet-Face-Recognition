import cv2
from PIL import Image

img = cv2.imread('./images/7.jpg')

size=(100,100)
oneimg=cv2.resize(img,size)
twoimg=cv2.resize(img,size,Image.ANTIALIAS)
threeimg=cv2.resize(img,size,Image.BICUBIC)
fourimg=cv2.resize(img,size,Image.BILINEAR)
fiveimg=cv2.resize(img,size,Image.NEAREST)

cv2.imshow('1',oneimg)
cv2.imshow('2',twoimg)
cv2.imshow('3',threeimg)
cv2.imshow('4',fourimg)
cv2.imshow('5',fiveimg)

cv2.waitKey(0)
cv2.destroyAllWindows()