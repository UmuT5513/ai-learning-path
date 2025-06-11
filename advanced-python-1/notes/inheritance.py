class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sınıfı türetildi!")

    def kendini_tanıt(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    pass


class Teacher(Person):
    pass


p1 = Person("umut", "agr", 22)
print(p1.name, p1.surname, p1.age)

s1 = Student("okan", "agr", 17)
print(s1.name, s1.surname, s1.age)

s1.kendini_tanıt()