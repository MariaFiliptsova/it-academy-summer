"""Даны два списка чисел.
Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""

# Решение 1
# spisok1 = [1, 2, 3, 4]
# spisok2 = [3, 4, 5, 6, 7, 1]
# spisok3 = [chislo for chislo in spisok1 if chislo in spisok2]
# print(len(spisok3))

# Решение 2
spisok1 = [1, 2, 3, 4]
spisok2 = [3, 4, 5, 6, 7, 1]
print(len(set(spisok1) & set(spisok2)))


"""Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков
"""

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6, 7, 1]
# list3 = [chislo for chislo in list1 if chislo not in list2]
# list4 = [tsifra for tsifra in list2 if tsifra not in list1]
# print(len(list3 + list4))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6, 7, 1]
print(len(set(list1) ^ set(list2)))
