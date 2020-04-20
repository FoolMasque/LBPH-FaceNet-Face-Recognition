
from PIL import Image

img=Image.open('./images/7.jpg')

size=(800,800)

one_img=img.resize(size)

two_img=img.resize(size,Image.ANTIALIAS)
three_img=img.resize(size,Image.BICUBIC)
four_img=img.resize(size,Image.BILINEAR)
five_img=img.resize(size,Image.NEAREST)

one_img.show()

two_img.show()
three_img.show()
four_img.show()
five_img.show()