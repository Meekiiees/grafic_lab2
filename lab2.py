from PIL import Image, ImageDraw

with open('DS5.txt', 'r') as f:
    data = [line.strip().split() for line in f]

data = [(int(y), int(x)) for x, y in data]

img = Image.new("RGB", (960, 540), (255, 255, 255))
draw = ImageDraw.Draw(img)

for x, y in data:
    draw.point((x, y), fill='black')

# Перевертаємо зображення на 180 градусів
img = img.rotate(180)

# Відзеркалюєм відносно вертикалі
img = img.transpose(Image.FLIP_LEFT_RIGHT)

img.save('result.png')
img.show()