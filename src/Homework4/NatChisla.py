"""Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""

# num1 = 10
# num2 = 8
# while num1 > 0 and num2 > 0:
#     if num1 > num2:
#         num1 = num1 % num2
#     else:
#         num2 = num2 % num1
# print(num1 + num2)

num1 = 8
num2 = 20
while num1 > 0 and num2 > 0:
    num1, num2 = num2, num1 % num2
print(num1)
