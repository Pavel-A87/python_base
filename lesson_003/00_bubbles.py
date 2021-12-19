# -*- coding: utf-8 -*-



# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# DO здесь ваш код
import simple_draw as sd

sd.resolution = (1200, 600)
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)

sd.pause()

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# DO здесь ваш код

import simple_draw as sd

sd.resolution = (1200, 600)

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)
point = sd.get_point(300, 300)
bubble(point=point, step=10)
sd.pause()

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


