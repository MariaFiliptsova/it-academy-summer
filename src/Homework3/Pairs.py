"""Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""
# Это решение за O(n), возможно оно выглядит как O(n**2),
# но в данном случае два for не являются вложенными.
# Не могли бы Вы объяснить, почему вас кажется, что
# данное решение это O(n**2)?

import math

spisok = '1 2 1 1 1'.split()
count_appearences = {}
number_of_pairs = 0
for i in spisok:
    count_appearences.update({i: spisok.count(i)})
for j in count_appearences.values():
    if j > 1:
        b_c = math.factorial(j) / (math.factorial(2) * math.factorial(j - 2))
        number_of_pairs += b_c
print(number_of_pairs)
