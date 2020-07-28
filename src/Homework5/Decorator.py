import time

'''Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
'''


def dec(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('results.txt', 'a') as f:
            f.write(func.__name__ + ' is called on ' + str(time.asctime()))
            f.write(' The result is ' + str(value) + '\n')
        return value

    return wrapper


@dec
def func(a, b):
    return a + b


print(func(2, 3))
print(func(1, 1))
