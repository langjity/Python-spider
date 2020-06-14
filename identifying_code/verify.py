import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr
# 解决问题：https://github.com/sirfz/tesserocr/issues/137
# windows下载安装：https://segmentfault.com/a/1190000014086067
from PIL import Image
# sudo CFLAGS="-mmacosx-version-min=10.14" pip3 install tesserocr
image = Image.open('cc.jpg')
result = tesserocr.image_to_text(image)
print(result)

'''
pip install tesserocr


第2中方法





pip install opencv-python

pip install pytesseract

https://blog.csdn.net/u010454030/article/details/80515501
'''

from PIL import Image
import pytesseract
import cv2 as cv

img_path = 'code.jpg'

# img_path='orgin.jpg'

# img_path='F:/fb/hpop.jpg'

# 依赖opencv
img = cv.imread(img_path)
text = pytesseract.image_to_string(image)

# 不依赖opencv写法
# text=pytesseract.image_to_string(Image.open(img_path))


print(text)
