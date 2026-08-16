# Day 4: 图片也是数字 —— 模拟图片滤镜

# 一张 3x3 的"图片"，每个像素是一个 0-255 的数字
image = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# 滤镜1：让每个像素变亮（加 20），但不能超过 255
brightened = []
for row in image:
    new_row = []
    for pixel in row:
        new_pixel = min(pixel + 20,255)# min 取较小值，防止超过255
        new_row.append(new_pixel)
    brightened.append(new_row)

print("原图",image)
print("提亮",brightened)

# 滤镜2：反色滤镜：255 - 像素值
inverted = []
for row in image:
    new_row = [255 - pixel for pixel in row]  # 这是 Python 的快捷写法（列表推导式）
    inverted.append(new_row)

print("反色",inverted)
