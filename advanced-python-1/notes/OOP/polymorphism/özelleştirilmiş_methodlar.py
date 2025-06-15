# POLYMORPHISM

# len() methodunun özelleştirilmesi
liste = [1,2,3]
print(len(liste))

str = "merhabalar"
print(len(str))


class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.yönetmen = director
        self.yıl = year
        self.süre = duration

m = Movie("hızlı ve öfkeli", "umut agr", "2005", 134)

print(m)
print(m.__repr__)
print(m.__repr__())


# __repr__() methoduna override yapıyoruz.
class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.yönetmen = director
        self.yıl = year
        self.süre = duration

    def __repr__(self):
        return f"{self.title}, {self.yönetmen} tarafından {self.yıl} yılında çekildi."

m = Movie("hızlı ve öfkeli", "umut agr", "2005", 134)

print(m)
print(m.__repr__)
print(m.__repr__())



# __len__() ekliyoruz.
class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.yönetmen = director
        self.yıl = year
        self.süre = duration

    def __repr__(self):
        return f"{self.title}, {self.yönetmen} tarafından {self.yıl} yılında çekildi."
    
    def __len__(self):
        return self.süre

m = Movie("hızlı ve öfkeli", "umut agr", "2005", 134)

print(len(m))


# __del__() ekleyelim. Bellekten silerken uygulanacak eylem.
class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.yönetmen = director
        self.yıl = year
        self.süre = duration

    def __del__(self):
        print("film silindi.")
        # eğer bir veri tabanından silinecekse kodlar bu aşamada yazılır.

m = Movie("hızlı ve öfkeli", "umut agr", "2005", 134)

del m