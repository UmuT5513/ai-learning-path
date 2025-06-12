# verileri gizlemek.
# değişkenlere ve methodlara erişimlere kısıtlamalar getirir.
# "_" ve "__"

class SuperClass:
    def __init__(self):
        self.__instance_attributes=1

    @property
    def get_instance_attributes(self):
        return self.__instance_attributes
    

class DerivedClass(SuperClass):
    def __init__(self):
        super().__init__()
        self.instance_attributes1 = self.get_instance_attributes # @propert decoratorü ekleyerek property şeklinde kullanılıyor.

        self.instance_attributes2 = self.__instance_attributes # hata verir!! böyle bir erişim yok 
        self.instance_attributes2 = self._SuperClass__instance_attributes #<-- doğrusu



d = DerivedClass()
print(d.instance_attributes1)
print(d.instance_attributes2)