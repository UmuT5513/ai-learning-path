#NOT: instance seviyesinde tanımlana methodlar

class CartItem:
    def __init__(self, myname, price, quantity):
        #instance attributes
        self.isim = myname
        self.fiyat = price
        self.miktar = quantity

    #instance methods
    def calculate_total(self):
        return self.fiyat*self.miktar

    def apply_discount(self, rate):
        '''indirim yüzdeliğini alarak indirim uygulanmış fiyatı döndürür.
            
            parameters:
                self: instance
                rate: indirim yüzdeliği. örn: %30 indirim uygulanmış fiyat için rate=30.
            
            returns:
                güncel fiyatın indirim uygulanmış hali.
        '''
        self.fiyat = self.fiyat*(1-rate/100)

#instance => nesne, örnek
item1=CartItem("telefon", 5000, 2)
item2=CartItem("pc", 100, 5)

print(item1.calculate_total())
item1.apply_discount(30)
print(item1.calculate_total())

