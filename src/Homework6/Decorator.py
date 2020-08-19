'''Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
'''


def calls(n=5):
    def dec(func):
        def wrapper(*args, **kwargs):
            nonlocal n
            try:
                for i in range(n):
                    print(func(*args, **kwargs))
            except Exception:
                raise Exception('TooManyErrors')
        return wrapper
    return dec


@calls(n=3)
def func(a, b):
    return a + b


func(2, 3)
func('t', 3)
