# -*- coding: utf-8 -*-



# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# DO здесь ваш код
import simple_draw as sd

sd.resolution = (1200, 600)
point = sd.get_point(100, 100)
radius = 50

for _ in range(3):
    sd.circle(center_position=point, radius=radius, width=2)
    radius += 5
sd.pause()

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# DO здесь ваш код

import simple_draw as sd

sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step

point = sd.get_point(100, 100)
bubble(point=point, step=10)
sd.pause()

# Нарисовать 10 пузырьков в ряд
# DO здесь ваш код

import simple_draw as sd

sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 55
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)
sd.pause()

# Нарисовать три ряда по 10 пузырьков
# DO здесь ваш код
import simple_draw as sd

sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 55
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)
sd.pause()


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# DO здесь ваш код

import simple_draw as sd

sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5)
sd.pause()



