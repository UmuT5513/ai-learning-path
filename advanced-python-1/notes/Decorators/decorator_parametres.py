def double(fn):
    def inner():
        fn()
        fn()
    return inner

def merhaba():
    print("merhaba")

def selam():
    print("selam")

sonuc = double(merhaba)
sonuc()
sonuc = double(selam)
sonuc()


def double(fn):
    def inner(*args, **kargs): # args ve kargs değişken saayıda parametre kabul eder anlamına gelir.
        fn(*args, **kargs)
        fn(*args, **kargs)
    return inner
@double
def merhaba():
    print("merhaba")

@double
def selam(isim):
    print("selam ", isim)

@double
def iyigunler():
    return "iyi günler"

merhaba()
selam("umut")




def double(fn):
    def inner(*args, **kargs): # args ve kargs değişken saayıda parametre kabul eder anlamına gelir.
        fn(*args, **kargs)
        return fn(*args, **kargs)
    return inner

@double
def iyigunler():
    return "iyi günler"

print("----------------")
sonuc = double(iyigunler)
print(sonuc())
print("----------------")
print(iyigunler())




