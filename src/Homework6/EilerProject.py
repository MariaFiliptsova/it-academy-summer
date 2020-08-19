import math
"""Определим f(n) как сумму факториалов всех цифр числа n.
Например, f(342) = 3! + 4! + 2! = 32.
Определим sf(n) как сумму цифр f(n). Таким образом, sf(342) = 3 + 2 = 5.
Определим g(i) как наименьшее положительное целое число n такое,
что sf(n) = i. Хотя sf(342) равно 5, sf(25) тоже равно 5, и можно показать,
что g(5) равно 25.
Определим sg(i) как сумму цифр g(i). Таким образом, sg(5) = 2 + 5 = 7.
Далее, можно показать, что g(20) равно 267, и ∑ sg(i) для 1 ≤ i ≤ 20 равна 156.
"""


def f(n):
    splited = [int(number) for number in str(n)]
    factorials = []
    for i in splited:
        fact = math.factorial(i)
        factorials.append(fact)
    return sum(factorials)


def sf(n):
    return sum([int(number) for number in str(f(n))])


def g(i):
    counter = 1
    sf_ = sf(counter)
    while sf_ != i:
        counter += 1
        sf_ = sf(counter)
    return counter


def sg(i):
    return sum([int(number) for number in str(g(i))])


def solution(start, end):
    return sum([sg(i) for i in range(start, end)])


print(solution(1, 21))
