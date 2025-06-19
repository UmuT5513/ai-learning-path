def bol(x, y):
    return x / y

try:
    bol(5,0)
    print("kod başarılı") # burası yürütülmez.
except ZeroDivisionError as err:
    print(err)
    print("kod basarısız! bol fonksiyonunda hata olustu")

try:
    bol(5,2)
    print("kod başarılı, except bloğu çalışmaz")
except ZeroDivisionError as err:
    print(err)


# built-in exception
num = 1
if num<5:
    raise ValueError("num 5'ten kucuk olamaz")

# custom exception class
class NumberError(Exception):
    pass

num=1
if num<5:
    raise NumberError("num 5'ten kucuk olamaz")


x=5
y=2
try:
    bol(x,y)
except ZeroDivisionError as err:
    print(err)
except TypeError as err:
    print(err)
else:
    print("kod basarılı")
finally:
    print("kod temizlendi...")