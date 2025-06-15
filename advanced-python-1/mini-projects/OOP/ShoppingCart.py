# TODO kupon kodu uygulandığında toplam sepet fiyatı üzerinden indirim yapılsın.

class CartItem:
    discount_rate=30
    item_count=0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."

    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(" ")
        return cls(name, int(price), int(quantity))

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

item1=CartItem("telefon", 5000, 2)
item2=CartItem("pc", 100, 5)
item3=CartItem.create_item("bisiklet 300 1")


class Coupon:
    def __init__(self, c, d):
        self.code = c
        self.discount = d
        #kupon geçerlilik tarihi

c1 = Coupon("code1", 50)
c2 = Coupon("code2", 40)
c3 = Coupon("code3", 30)



class ShoppingCart:
    '''
        class attributes:
            list : coupon_list
        
        instance attributes:
            list : item list
            
        class methods:
            list : get_coupons()
            Coupon : get_coupon()

        instance methods:
            add_item()
            display_items()
            int : calculate_totals()
            remove_item()
            list : clear()
            apply_coupon()
    '''
    coupon_list = [c1,c2,c3]
    

    def __init__(self, liste):
        self.list = liste
    
    def add_item(self, item):
        '''sepete ürün ekler.'''
        self.list.append(item)

    def display_items(self):
        '''sepetteki ürünlerin özelliklerini print eder.'''
        for i in self.list:
            print(f"Ürün:{i.name}\nFiyat:{i.price}TL\nAdet:{i.quantity}\n")

    def calculate_totals(self):
        '''toplam sepet tutarını döndürür.'''
        return f"Toplam sepet tutarı: {sum([item.calculate_total() for item in self.list])}TL"

    def remove_item(self, deleted_item):
        self.list = [item for item in self.list if item != deleted_item] # self.list içindeki itemlerdan deleted_item a eşit olmayanları al eski listede güncelle.

    def clear(self):
        '''sepetteki tüm ürünleri siler!'''
        self.list = []

    @classmethod
    def get_coupons():
        '''kuponların codelarını liste olarak döndürür.'''
        return [coupon.code for coupon in ShoppingCart.coupon_list]

    @classmethod
    def get_coupon(code):
        '''verilen code a göre uygun coupon nesnesi döndürür.'''
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))

    def apply_coupon(self, code, type="birleşik"):
        '''
        kuponun varlığını kontrol edip tüm ürünlere uygular.

        parametres:
            string : type - "ayrı" ise kuponu ürünlere teker teker uygular, "toplam" ise total fiyat üzerinden uygular.
            string : code 

        return:
            eğer "type=birleşik" seçilirse toplam fiyatın indirimli halini döndürür.
            eğer "type=ayrı ayrı" seçilirse her bir ürünün fiyatına ayrı ayrı indirim yapar fiyatları günceller, toplamlarını döndürür.
            default : birleşik
        '''

        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"geçersiz kupon kodu: {code}")
        
        coupon = ShoppingCart.get_coupon(code)

        if (type=="ayrı ayrı"):
            # kupon kodunu tüm ürünlere uygular
            for index in range(len(self.list)):
                self.list[index].price = self.list[index].price * coupon.discount
                return sum(self.list)
        elif (type=="birleşik"):
            for index in range(len(self.list)):
                sum=0
                sum += self.list[index].price
                return sum * coupon.discount
        

sc = ShoppingCart([item1, item2])
sc.add_item(item3)
sc.display_items()

print(sc.calculate_totals())

#sc.clear()

print(ShoppingCart.get_coupons())
print(ShoppingCart.get_coupon("code1"))
sc.apply_coupon("code2")

