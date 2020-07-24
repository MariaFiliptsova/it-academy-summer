"""Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов
— названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
Примеры

Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa


3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""

N = int(input('Enter number of countries\n'))
countries_with_cities = {}
repeated_cities = {}
for i in range(N):
    country, *cities = input('Enter country and its cities\n').split()
    for city in cities:
        if city not in countries_with_cities:
            countries_with_cities.update({city: country})
        else:
            repeated_cities.update({city: country})
M = int(input('Enter the number of cities\n'))
list_of_cities = []
for j in range(M):
    list_of_cities.append(input('Enter a city\n'))

for y in list_of_cities:
    if y in countries_with_cities:
        print(y + ' is in ' + countries_with_cities[y])
        if y in repeated_cities:
            print('and also in ' + repeated_cities[y])
    else:
        print('No idea where this city is')
