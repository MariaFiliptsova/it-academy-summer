"""Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""
spisok = [0, 8, 21, 0, 17, 0, 25]
print(spisok)
for i in spisok:
    if not i:
        spisok.remove(i)
        spisok.append(i)
print(spisok)
