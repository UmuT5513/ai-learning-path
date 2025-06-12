class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            ValueError("ürün fiyatı negatif değer olamaz!")

    def set_price(self, value):
        if value >= 0:
            self._price = value
        else:
            ValueError("ürün fiyatı negatif değer olamaz!")

    def get_price(self):
        return self._price


p = Product("Iphone", 80000)

print(p.get_price())
p.set_price(30000)

print(p.get_price())


class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            ValueError("ürün fiyatı negatif değer olamaz!")

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            ValueError("ürün fiyatı negatif değer olamaz!")
    

p = Product("Iphone", 50000)
print(p.price)
p.price=90000
print(p.price)