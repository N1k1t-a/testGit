class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{type(self).__name__}(name={self.name!r}, price={self.price})"


class Laptop(Product):
    pass


class Smartphone(Product):
    pass


product1 = Product("laptop 1", 1999)
product2 = Product("smartfone 1", 999)
# если вписывать туда лаптоп и смартфоне, то поменяется только название класса
print(product1)  # Product(name='laptop 1', price=1999)
print(product2)  # Product(name='smartfone 1', price=999)

