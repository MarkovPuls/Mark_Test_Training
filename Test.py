def percents(x, y):
    """Комментарии пишутся через тройные скобки"""
    """Пример: сколько процентов от x составляет y"""
    one_percent = x / 100
    result = y / one_percent
    return result


def print_percents(x, y):
    """Пример: сколько процентов от x составляет y"""
    print(str(y) + " is " + str(percents(x, y)) + "% of " + str(x))


percents(200,50)
