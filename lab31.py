import cv2
import numpy as np
from PIL import Image, ImageDraw

# Загрузите данные из файла
with open('DS5.txt', 'r') as f:
    data = [line.strip().split() for line in f]

data = [(int(y), int(x)) for x, y in data]

# Создайте матрицу преобразования
alpha = 30  # Угол поворота
M = cv2.getRotationMatrix2D((480, 480), alpha, 1)

# Примените матрицу преобразования к данным
data = np.array(data)
data = np.hstack((data, np.ones((data.shape[0], 1))))
data = np.dot(M, data.T).T[:, :2]

# Округлите значения до двух знаков после запятой
data = np.around(data, decimals=2)

# Создайте изображение
img = Image.new("RGB", (960, 540), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Отобразите данные
for x, y in data:
    draw.point((x, y), fill='black')

# Переверните изображение на 180 градусов
img = img.rotate(180)

# Отзеркальте изображение по вертикали
img = img.transpose(Image.FLIP_LEFT_RIGHT)

# Сохраните изображение
img.save('result.png')

# Отобразите изображение
img.show()