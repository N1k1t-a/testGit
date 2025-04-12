from functools import partial

# Тема, которую мы импортнули нужна для того, чтобы, если нам чет оченб часто надо
# прописывать, то мы можем сделать дефолтное значение вне функции. Так энивей пизде просто получается


def say_hello(name, greeting) -> None:
    msg = f'{name}, даун, {greeting}'
    print(msg)


say_hi = partial(say_hello, greeting='Hi')
print(say_hi)
say_hello('HEllo', 'Olga')
say_hello('HEllo', 'Max')
say_hello('HEllo', 'Max')
say_hello('HEllo', 'Vladimir')
say_hello('HEllo', 'ANton')

say_hi('Ol')
say_hi('Max')
say_hi('Andrey')
say_hi('Anton')
say_hi('гандон')
