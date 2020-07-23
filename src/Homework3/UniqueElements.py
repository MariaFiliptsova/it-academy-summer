"""Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""
# Решение 1
# spisok = [1, 3, 'a', 'a', 3, 4, 10, 2, 'word', 10]
# unique_elements = []
# for i in spisok:
#     n = spisok.count(i)
#     if n == 1:
#         unique_elements.append(i)
# print(unique_elements)

# Решение 2

spisok = [1, 3, 'a', 'a', 3, 4, 3, 10, 2, 'word', 10]
once = set()
more = set()
dict = {}
res = []
for el in spisok:
    if el not in once:
        if el not in more:
            once.add(el)
    else:
        more.add(el)
        once.remove(el)
for i in once:
    index = spisok.index(i)
    dict.update({index: i})
spisok_indexes = list(dict.keys())
spisok_indexes.sort()
for j in spisok_indexes:
    res.append(dict[j])
print(res)
