# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# DO здесь ваш код
import math

while True:
    a = int(input("Inter value A:"))
    b = int(input("Inter value B:"))

    float_value = a / b
    print(float_value)
    int_value = math.trunc(float_value)
    print(int_value)

    if a < b:
        print("Wrong values! 'A' must be a bigger then 'B'")
    elif float_value > int_value:
        print("Кэп, фсё прапалО!!!!Мы не знаем куда деть лишние цифирики")
    else:
        print("Целочисленное деление ", a, "на ", b, "дает ", int_value)
