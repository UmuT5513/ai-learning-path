def usalma(taban):
    def inner(üs):
        return taban**üs
    return inner


sonuc = usalma(2)(4)
print(sonuc)

fonksyion = usalma(2)
sonuc = fonksyion(4)
print(sonuc)


def yetki_sorgulama(sayfa):
    '''kullanıcı bir web uygulamasında bir sayfaya gitmek istiyor. Rolu/rütbesi buna uygun mu? uyugnsa erişim ver.'''
    def inner(role):
        if role == "Admin":
            return f"{role} rolü {sayfa} sayfasına erişim sağlayabilir."
        else:
            return f"{role} rolü {sayfa} sayfasına erişimi sağlayamaz."
        
    return inner

yetki = yetki_sorgulama("'ürün güncelleme'")
sonuc = yetki("Admin")
print(sonuc)

sonuc = yetki_sorgulama("'ürün güncelleme'")("Öğrenci")
print(sonuc)





def islem(islem_adi):
    def toplam(*args):
        top=0
        for i in args:
            top += i
        return top

    def carpım(*args):
        carp=1
        for i in args:
            carp *= i
        return carp
    
    if islem_adi == "toplama":
        return toplam
    else:
        return carpım


toplama = islem("toplama")
carpma = islem("carpma")

sonuc = toplama(10,20)
print(sonuc)

sonuc = carpma(10,20)
print(sonuc)