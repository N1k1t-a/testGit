import functools

# кэш - это быстрая временная память
# например мы чет посчитали, это сохранилось в кэш, потом при повторном вызове это не
# считается заново, а берется из памяти

@functools.lru_cache(3)
def sum_it(a, b):
    '''sum two number'''
    print(f'calc: {a} + {b}')
    return  a + b


print(sum_it(2,6))
print(sum_it(2,6))
# calc: 2 + 6
# 8 мы видим, что он сначала посчитал, а потом вывел ответ на экран
# 8 а тут мы можем наблюдать, что он ничего не считал, а просто сразу же вывел значение на экран
# print(sum_it(2,7))
# print(sum_it(2,7))
# print(sum_it(2,9))