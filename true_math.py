def divide(first, second):
    from math import inf    # Импортируем inf  из библиотеки math
    if second == 0:
        return inf          # Возвращаем положительную бесконечность
    a2 = first / second
    return a2               # Вовзращаем а2