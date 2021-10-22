#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

citys = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

# DO здесь заполнение словаря
from pprint import pprint
distances = {}
moscow = citys['Moscow']
london = citys['London']
paris = citys['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2  ) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2  ) ** .5
paris_london = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2  ) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = paris_london

distances['Paris'] = {}
distances['Paris']['London'] = paris_london
distances['Paris']['Moscow'] = moscow_paris


pprint(distances)




