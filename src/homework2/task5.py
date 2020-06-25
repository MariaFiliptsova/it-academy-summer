"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """
    # write your code here
    num1 = 1
    num2 = 1
    i = 0
    if n == 0:
        return 0
    else:
        while i < n - 2:
            num1, num2 = num2, (num1 + num2)
            i = i + 1

    return num2  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 4
    print(fibonacci(n))
