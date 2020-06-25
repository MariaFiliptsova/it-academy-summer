"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    # write your code here
    import string
    str_ = str_.split()
    longest_word = None
    longest_word_length = 0
    punctuation_symbols = string.punctuation
    for current_word in str_:
        without_punc = current_word.strip(punctuation_symbols)
        current_word_length = len(without_punc)
        if current_word_length > longest_word_length:
            longest_word = without_punc
            longest_word_length = current_word_length

    return longest_word


# write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'eh, bum vo, an'
    print(longest_word(str_))
