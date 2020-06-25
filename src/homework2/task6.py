"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    # write your code here
    new_number = 0
    copy_n = n
    chisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if n % 10 == 0 or n in chisla:
        print(False)
    else:
        while n > 0:
            get_number = n % 10
            new_number = get_number + (new_number * 10)
            n = n // 10
        if (copy_n == new_number):
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 101
    print(palindrom(n))
