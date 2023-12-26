from PIL import Image, ImageDraw, ImageOps
import math

def rotate_point(point):
    x, y = point
    cx, cy = (480, 480)
    angle_rad = math.radians(60)
    x_new = round(cx + (x - cx) * math.cos(angle_rad) - (y - cy) * math.sin(angle_rad), 0)
    y_new = round(cy + (x - cx) * math.sin(angle_rad) + (y - cy) * math.cos(angle_rad), 0)
    return int(x_new), int(y_new)

with open('DS5.txt', 'r') as f:
    data = [line.strip().split() for line in f]

data = [(int(y), int(x)) for x, y in data]

img = Image.new("RGB", (960, 540), (255, 255, 255))
draw = ImageDraw.Draw(img)

new_img = Image.new("RGB", (960, 540), (255, 255, 255))
draw_new = ImageDraw.Draw(new_img)

for x, y in data:
    x_new, y_new = rotate_point((x, y))
    draw_new.point((x_new, y_new), fill='blue')

new_img = new_img.rotate(180)
new_img = new_img.transpose(Image.FLIP_LEFT_RIGHT)

new_img.save('result.png')
new_img.show()
