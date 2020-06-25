"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".

   Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""


def sub_string(str_):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """

    # write your code here
    line_without_space = str_.replace(" ", "")
    spisok_symbolov = []
    for symbol in line_without_space:
        if symbol not in spisok_symbolov:
            spisok_symbolov.append(symbol)
    return ''.join(spisok_symbolov)


# write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'this is my sentence'
    print(sub_string(str_))
