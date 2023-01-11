from PIL import Image
from PIL import ImageFilter
img=Image.open("mr.jpg")
blur_img=img.filter(ImageFilter.GaussianBlur(5))
blur_img.show()