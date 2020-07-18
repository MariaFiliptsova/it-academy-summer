'''Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_ranges(spisok=[0, 1, 2, 3, 4, 7, 8, 10]):
    spisok.append(spisok[-1] + 2)
    start = spisok[0]
    number_before = spisok[0]
    res = []
    for number in spisok[1:]:
        if number == number_before + 1:
            number_before = number
        else:
            if start == number_before:
                res.append(str(start))
                number_before = number
                start = number
            else:
                res.append(str(start) + '-' + str(number_before))
                number_before = number
                start = number
    return ','.join(res)


print(get_ranges())
