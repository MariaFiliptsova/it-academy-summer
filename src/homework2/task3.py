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
    length_of_line = len(line_without_space)
    new_line = []
    for symbol in line_without_space:
        if symbol not in new_line:
            new_line.append(symbol)
    return ''.join(new_line)


# write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'this is my sentence'
    print(sub_string(str_))
