# iterator oluşturan fonksiyon

def counter(max):
    sayi = 1


    while sayi <= max:
        yield sayi
        sayi += 1
    
# yield anahtar kelimesi ile fonksiyon bir generator nesnesi döner.
sonuc = counter(10)
print(next(sonuc))  # 1
print(next(sonuc))  # 2    
print(next(sonuc))  # 3
print(next(sonuc))  # 4 
# bilgiler bellekte yer tutmadan bu şekilde okunur. Yani bellekte tüm listeyi tutmaz.
# for ile de kullanılabilir.
for i in sonuc:
    print(i)  # 5, 6, 7, 8, 9, 10



generator = counter(10)
print(generator)
print(dir(generator))  # __iter__, __next__ gibi metodlar var
# generator nesnesi iterable olduğu için for ile de kullanılabilir.

# generator ile iterable arasındaki fark
# generator, iterable bir nesnedir ama iterable bir nesne generator değildir.

# generator, bellekte tüm veriyi tutmaz, sadece ihtiyaç duyulduğunda üretir.
# iterable ise bellekte tüm veriyi tutar ve her seferinde aynı veriyi döner.

# generator ile iterable arasındaki farkı anlamak için aşağıdaki örneği inceleyebilirsiniz.
def iterable_example():
    return [1, 2, 3, 4, 5]
def generator_example():
    for i in range(1, 6):
        yield i

iterable = iterable_example()
generator = generator_example()

print(iterable)  # [1, 2, 3, 4, 5]
print(generator)  # <generator object generator_example at 0x...>
print(next(generator))  # 1
print(next(generator))  # 2 
print(next(generator))  # 3
print(next(generator))  # 4

# iterable üzerinde for döngüsü ile iterasyon yapılabilir
for i in iterable:
    print(i)  # yalnızca 3, 4, 5

# generator üzerinde for döngüsü ile iterasyon yapılabilir
for i in generator: 
    print(i)  # yalnızca 5 yazdırır. # çünkü generator üzerinde iterasyon yapıldığında, generator nesnesi tükenir.
# Bu nedenle, generator üzerinde iterasyon yapıldıktan sonra, tekrar next() ile erişim yapılamaz.
# Eğer generator üzerinde tekrar iterasyon yapmak isterseniz, yeni bir generator nesnesi oluşturmanız gerekir.
# Örneğin:
new_generator = generator_example()
for i in new_generator:
    print(i)  # 1, 2, 3, 4, 5

# generator'lar, bellek kullanımını optimize etmek için kullanılır.
# Özellikle büyük veri setleri ile çalışırken, tüm veriyi bellekte tutmak yerine, ihtiyaç duyulduğunda veriyi üretmek daha verimlidir.



# list comprehension ile generator oluşturma
list_comprehension = [i for i in range(1, 11)]
print(list_comprehension)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator_comprehension = (i for i in range(1, 11))
print(generator_comprehension)  # <generator object <genexpr> at 0x...>
# generator comprehension ile oluşturulan generator nesnesi üzerinde iterasyon yapılabilir
print(next(generator_comprehension))  # 1
print(next(generator_comprehension))  # 2

