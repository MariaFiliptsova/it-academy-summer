import math

'''Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''
'''#Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар'''


def pairs(spisok=[1, 1, 1]):
    count_appearences = {}
    number_of_pairs = 0
    for i in spisok:
        count_appearences.update({i: spisok.count(i)})
        for j in count_appearences.values():
            if j > 1:
                b_c = math.factorial(j) / \
                      (math.factorial(2) * math.factorial(j - 2))
                number_of_pairs += b_c
                return number_of_pairs


'''Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
'''


def ordered(data=[0, 1, 0, 3]):
    for i in data:
        if i == 0:
            data.remove(i)
            data.append(i)
    return data


def runner(*args):
    if len(args) == 0:
        print(pairs())
        print(ordered())
    else:
        for arg in args:
            if arg == 'pairs':
                print(pairs())
            elif arg == 'ordered':
                print(ordered())
            else:
                print('Unknown function')


runner()
runner('pairs')
runner('ordered', 'pairs')
runner('func')
