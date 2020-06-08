"""Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""
spisok = [1, 3, 'a', 'a', 3, 4, 10, 2, 'slovo', 10]
new_spisok = []
print(spisok)
for i in spisok:
    n = spisok.count(i)
    if n == 1:
        new_spisok.append(i)
print(new_spisok)
