'''Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


def powers(n=10):
    pow = 0
    while (n >> pow) > 1:
        pow += 1
    if (n - (2 ** pow)) < ((2 ** (pow + 1)) - n):
        return (2 ** pow)
    else:
        return (2 ** (pow + 1))


print(powers(10))
print(powers(20))
print(powers(1))
print(powers(13))

'''Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).'''


def devider(n=24):
    pow = 0
    while (n >> pow) >= 1 and (n % 2 ** pow) == 0:
        pow += 1
    return 2 ** (pow - 1)


print(devider(10))
print(devider(16))
print(devider(12))
