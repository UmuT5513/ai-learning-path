# otomatiğe bağlanmak istenen fonksiyonlar


def selamlama(fn):
    def inner(ad):
        print("hoş geldiniz")
        fn(ad)
        print("görüşmek üzere")
    return inner

@selamlama
def guno(ad):
    print(f"günaydın benim adım {ad}")
    
@selamlama
def iyigunler(ad):
    print(f"iyi günler benim adım {ad}")


# sonuc = selamlama(guno)
# sonuc()
# sonuc = selamlama(iyigunler)
# sonuc()

print("\n")
guno("ali")
iyigunler("umut")
# decorator sayesinde bu şekilde yapılabilir.
