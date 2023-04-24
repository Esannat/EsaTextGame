from PIL import Image
import json

# 把位图放到source/maps中，filename是去掉后缀的文件名
filename = "./source/maps/labyrinth2"
image = Image.open(filename + ".bmp")

width = image.width
height = image.height

res = []
i = 0
while i < height:
    j = 0
    while j < width:
        pixel = image.getpixel((j,i))
        if pixel == (34, 177, 76):
            letter = 'w'
        elif pixel == (0, 0, 0):
            letter = 's'
        elif pixel == (237, 28, 36):
            letter = 'c'
        elif pixel == (63, 72, 204):
            letter = 'd'
        res.append(letter)
        j += 1
    i += 1
res = ''.join(res)

obj = {"width":width, "height":height, "seq": res}
with open(filename + ".json", "w", encoding="utf-8") as f:
    json.dump(obj, f)

