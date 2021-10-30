#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# DO здесь ваш код

garden_set = set(garden)
meadow_set = set(meadow)
print(garden_set)
print(meadow_set)

# выведите на консоль все виды цветов
# DO здесь ваш код


all_flowers = set(garden + meadow)
print(all_flowers)

# выведите на консоль те, которые растут и там и там
# DO здесь ваш код

and_garden_and_meadow = garden_set.intersection(meadow_set)
print(and_garden_and_meadow)


# выведите на консоль те, которые растут в саду, но не растут на лугу
# DO здесь ваш код

only_garden = garden_set.difference(meadow_set)
print(only_garden)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# DO здесь ваш код

only_meadow =meadow_set.difference(garden_set)
print(only_meadow)

