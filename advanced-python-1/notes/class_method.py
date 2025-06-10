#NOT: class seviyesinde tanımlanan methodlar

class CartItem:
    discount_rate=30
    item_count=0

    @classmethod
    def display_item_count():
        return f"{CartItem.item_count} tane ürün oluşturuldu."

    @classmethod
    def create_item(data_str):
        name, price, quantity = data_str.split(" ")
        return CartItem(name, price, quantity)

    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quantity = q
        CartItem.item_count += 1 #nesne sayısını gösterir.

    def calculate_total(self):
        return self.price*self.quantity

    def apply_discount(self):
        '''indirim yüzdeliğini alarak indirim uygulanmış fiyatı döndürür.
            
            parameters:
                self: instance
                rate: indirim yüzdeliği. örn: %30 indirim uygulanmış fiyat için rate=30.
            
            returns:
                güncel fiyatın indirim uygulanmış hali.
        '''
        self.price = self.price*(1-CartItem.discount_rate/100)


print(CartItem.display_item_count())
item1=CartItem("telefon", 5000, 2)
item2=CartItem("pc", 100, 5)
print(CartItem.display_item_count())
item3=CartItem.create_item("bisiklet 300 1")

