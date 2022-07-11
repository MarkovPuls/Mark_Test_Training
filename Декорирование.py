def decor():
    def decorator(func):
        def wrap(*args, **kwargs):
            print('Начало выполнения')
            print(args, kwargs)
            return func(*args, **kwargs)

        return wrap

    return decorator


@decor()
def summ(a, b, some_kwargs=3):
    if some_kwargs:
        return a + b + some_kwargs
    return a + b


summ(1, 2, some_kwargs=0)
