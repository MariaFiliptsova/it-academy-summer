"""Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French


Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""

N = int(input('Enter a number of students\n'))
all_students = set()
all_languages = set()
for i in range(int(N)):
    M = int(input('Number of spoken languages\n'))
    spoken_languages = {input('What language\n') for j in range(M)}
    all_languages.update(spoken_languages)
    if len(all_students) == 0:
        all_students.update(spoken_languages)
    else:
        all_students &= spoken_languages
print(len(all_students))
print(' '.join(all_students))
print(len(all_languages))
print(' '.join(all_languages))
