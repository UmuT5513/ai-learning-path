class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sınıfı türetildi!")

    def kendini_tanıt(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self,name,surname,age, ogr_no):
        super().__init__(name, surname, age)
        #Person.__init__(self,name,surname,age)
        self.number = ogr_no
        print("student sınıfı türetildi.")

    def ders_calıs(self):
        print(f"{self.name} ders calıstı!")

    def kendini_tanıt(self):
        print(self.name, self.surname, self.age, self.number)


class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name,surname,age)
        self.branş = branch
        print("teacher sınıfı türetildi.")

    def ders_anlat(self):
        print(f"{self.name}, {self.branş} anlattı!")


p1 = Person("umut", "agr", 22)
print("-----------------------------")
s1 = Student("okan", "agr", 17, 225)
print("-----------------------------")
t1 = Teacher("buglem", "agr", 13, "fizik")

s1.ders_calıs()
t1.ders_anlat()
