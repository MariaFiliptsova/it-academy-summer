"""Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""
import math

spisok = '1 1 1 1 23 4 2 3 2'.split()
count_appearences = {}
number_of_pairs = 0
for i in spisok:
    count_appearences.update({i: spisok.count(i)})
print(count_appearences)
for j in count_appearences.values():
    if j > 1:
        # формулу биномиального коэффицента подсказали математики на работе
        b_c = math.factorial(j) / (math.factorial(2) * math.factorial(j - 2))
        number_of_pairs += b_c
print(number_of_pairs)
