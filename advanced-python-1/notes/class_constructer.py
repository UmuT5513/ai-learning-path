class CartItem:
    def __init__(self, myname, price, quantity):
        #instance attributes
        self.isim = myname
        self.fiyat = price
        self.miktar = quantity

#instance => nesne, örnek
item1=CartItem("telefon", 5000, 2)
item2=CartItem("pc", 100, 5)

