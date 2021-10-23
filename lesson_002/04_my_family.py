#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['husband', 'wife', 'daughter', 'son']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Pavel', 182],
    ['Julia', 167],
    ['Elizaveta', 165],
    ['Mark', 87]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ', my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
# sum_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
sum_height = sum([item[1] for item in my_family_height])
print('Общий рост семьи - ', sum_height, 'см')