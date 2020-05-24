"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
   цена, а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    cost = s * (m * 100 + n)
    rubles_part = cost // 100
    kopecks_part = cost % 100
    result = str(rubles_part) + ' rubles ' + str(kopecks_part) + ' kopecks'
    return result  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = 2, 20, 2
    print(total_sum(m, n, s))
