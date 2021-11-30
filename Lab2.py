#PIL - бібліотека для роботи з растровою графікою, re - бібліотека для роботи з regex
from PIL import Image, ImageDraw
import re

canvas = Image.new('RGBA', (540, 960), 'yellow') # - створюємо пустий жовтий лист з указаним resolution
idraw = ImageDraw.Draw(canvas) # - забезпечує просту 2D графіку для нашого обєкта

file = open("DS2.txt") # - відкриважмо файл
strfile = file.readlines() # - зчитауєио файл
strFileSplit = [] # - створюємо масив
# - заповнення масиву точками, findall - використовується для пошуку всіх непересічних збігів в шаблоні.
for i in range(len(strfile)):
    strFileSplit.append(re.findall(r'\d+', strfile[i]))
# - виводимо маисв на пустий лист чорним кольором
for j in range(len(strFileSplit)):
    idraw.point((int(strFileSplit[j][0]), int(strFileSplit[j][1])), fill ="black")

canvas.save("labpic.png", "PNG") # - зберігання файлу
canvas.show() # - показ результату
