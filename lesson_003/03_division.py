# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# DO здесь ваш код
while True:
    a = int(input("Inter value A:"))
    b = int(input("Inter value B:"))
    if a < b:
        print("Wrong values! 'A' must be a bigger then 'B'")
    elif a > b:
        x = a / b
        if type(x) == int:
            print(x)
        else:
            print("bbb")