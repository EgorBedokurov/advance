import random
from functools import lru_cache

def cache(f):
    def deco(*args):
        if args in deco._cache:
            return deco._cache[args]
        result = f(*args)
        deco._cache[args] = result
        return result
    deco._cache = {}
    return deco


@cache
def arf_pr(n, d):
    start_namb = 1
    return start_namb + (n-1)*d

element = int(input('Введите номер искомого элемента прогрессии : '))
step = int(input('Введи разность прогрессии : '))
value = arf_pr(element, step)
print(str(element)+' сумма арифметической прогрессии равна ' + str(value))

