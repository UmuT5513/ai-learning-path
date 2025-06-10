class CartItem:
    discount_rate=30
    item_count=0

    def __init__(self, name, price, quantity):
        #instance attributes
        self.isim = name
        self.fiyat = price
        self.miktar = quantity
        CartItem.item_count += 1 #nesne sayısını gösterir.

    #instance methods
    def calculate_total(self):
        return self.fiyat*self.miktar

    def apply_discount(self):
        '''indirim yüzdeliğini alarak indirim uygulanmış fiyatı döndürür.
            
            parameters:
                self: instance
                rate: indirim yüzdeliği. örn: %30 indirim uygulanmış fiyat için rate=30.
            
            returns:
                güncel fiyatın indirim uygulanmış hali.
        '''
        self.fiyat = self.fiyat*(1-CartItem.discount_rate/100)

#instance => nesne, örnek
item1=CartItem("telefon", 5000, 2)
item2=CartItem("pc", 100, 5)


# hem nesne hem class üzerinden erişim
print(item1.discount_rate)
print(CartItem.discount_rate)


#class üzerinden tanımlandığının bir başksa göstergesi
# __dict__ --> magic attributes
print(item1.__dict__)
print(CartItem.__dict__)


