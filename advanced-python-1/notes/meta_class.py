
#1 type ile class oluşturma, değişken tanımlama
TestMetaClass = type("Test", (), {"name":"umut", "age": 22})
t = TestMetaClass()
print(t.name)
print(t.age)



#2 tuple ile miras alma
def show(self):
    return "merhaba"

BaseMetaClass = type("BaseClass",(), {"show" : show})
TestMetaClass = type("Test", (BaseMetaClass,), {"name":"umut", "age": 22})
t = TestMetaClass()
print(t.show())