# for döngüsü iterable olan nesne iteratore çevirme işlemini arka planda yapar. iter() ile bu manuel olarak gerçekleştirilir.
# sayilar : iterable bir nesne

# Bir liste (iterable) üzerinde for döngüsü ile gezinme
sayilar = [1,2,3,4]
for i in sayilar:
    print(i)  # 1, 2, 3, 4 yazdırılır

# Bir string (iterable) üzerinde for döngüsü ile gezinme
text = "BTK AKADEMİ"
for letter in text:
    print(letter)  # Her harfi tek tek yazdırır

# Hatalı kullanım örneği:
sayilar = [1,2,3,4]
# next() fonksiyonu doğrudan iterable üzerinde çalışmaz, iterator olması gerekir
print(next(sayilar)) # TypeError: 'list' object is not an iterator

# Doğru kullanım: iter() ile iterator oluşturulur
iterator = iter(sayilar)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
print(next(iterator))  # StopIteration hatası verir. listede 4 eleman var.

# Iterator ile tüm elemanları döngüyle çekmek:
iterator = iter(sayilar)  # Yeni bir iterator oluşturduk
while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break  # Eleman kalmayınca döngü kırılır


