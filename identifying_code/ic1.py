from PIL import Image
image = Image.open('code.jpg')
import pytesseract

text = pytesseract.image_to_string(image)

print(text)

# 模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度
# https://blog.csdn.net/icamera0/article/details/50843172
image = image.convert('L')
threshold = 127  # 阈值
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()

result = pytesseract.image_to_string(image)
print(result)
