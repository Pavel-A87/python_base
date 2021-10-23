#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]


# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# DO здесь ваш код

zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# DO здесь ваш код
zoo.extend(birds)
print(zoo)


# уберите слона
#  и выведите список на консоль
# DO здесь ваш код

zoo.pop(3)
#  zoo.remove('elephant') //alternate
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# DO здесь ваш код

index_lion = zoo.index('lion')
index_lark = zoo.index('lark')
print('Лев сидит в клетке №', index_lion+1)
print('Жаворонок сидит в клетке №', index_lark+1)
