# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# from typing import Tuple
# DO здесь ваш код

month_31_day = (1, 3, 5, 8, 7, 10, 12)
month_30_day = (4, 6, 9, 11)
month_28_day = (2,)
while 1 > 0:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month = int(user_input)
    print('Вы ввели', month)
    if month in month_31_day:
        print("31")
    elif month in month_30_day:
        print("30")
    elif month in month_28_day:
        print("28")
    elif month >= 13 or month <= 0:
        print("Неправильный месяц, должен быть положительным числом от 1 до 12")
