# 1 Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
spisok = [c + d for c in ['a', 'b'] for d in ['b', 'c', 'd']]
print(spisok)

# 2 Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
sliced_list = spisok[0::2]
print(sliced_list)

# 3 Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
spisok2 = [str(c) + d for c in range(1, 5) for d in ['a']]
print(spisok2)

# 4 Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
print(spisok2.pop(1))

# 5 Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.
copied_list = spisok2[:]
copied_list.insert(1, '2a')
print(copied_list)
print(spisok2)
