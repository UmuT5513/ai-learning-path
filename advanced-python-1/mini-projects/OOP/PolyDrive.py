#“PolyDrive”; farklı araç tiplerinin (otomobil, motosiklet, kamyon, vb.) ortak bir Vehicle taban 
#sınıfından türetilip, her birinin kendi motor çalıştırma davranışını sergilediği; miras ve çok 
#biçimlilik kavramlarını (inheritance & polymorphism) pekiştiren öğretici bir konsol/GUI uygulamasıdır.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    is_running = False
    
    def __init__(self, model):
        self.model = model
        self.is_running = Vehicle.is_running

    def __repr__(self):
        '''Sınıf ekrana basıldığında okunabilir bir metin döndürür. __repr__ methoduna override edilmiştir.'''
        return f"<Vehicle: {self.model}, running={self.is_running}>"
    
    def start_engine(self):
        pass

    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, model, id):
        #Vehicle.__init__(self, model, is_running)
        super().__init__(model)
        self.id = id

    def start_engine(self):
        self.is_running=True
        print(f"Vrooom! {self.model} çalışıyor...")

    def stop_engine(self):
        self.is_running=False
        print(f"Motor durdu! {self.model}")

    def __repr__(self):
        return super().__repr__()
    

class Motorcycle(Vehicle):
    def __init__(self, model, id):
        super().__init__(model)
        self.id = id

    def start_engine(self):
        self.is_running=True
        print(f"Brmmmm! {self.model} çalışıyor...")

    def stop_engine(self):
        self.is_running=False
        print(f"Motor durdu! {self.model}")

    def __repr__(self):
        return super().__repr__()
    

class Truck(Vehicle):
    def __init__(self, model, id):
        super().__init__(model)
        self.id = id

    def start_engine(self):
        self.is_running=True
        print(f"Gümbürrrr! {self.model} çalışıyor...")

    def stop_engine(self):
        self.is_running=False
        print(f"Motor durdu! {self.model}")

    def __repr__(self):
        return super().__repr__()


t1 = Truck("MAN", 1001)
m1 = Motorcycle("Suzuki", 2001)
c1 = Car("Toyota", 3001)
t3 = Truck("man", 1003)



class FleetManager():
    def __init__(self, vehicle_list):
        self.list = vehicle_list

    def start_all(self):
        for i in range(len(self.list)):
            self.list[i].start_engine()
        print("Tüm araçlar çalışmakta!")        

    def stop_all(self):
        for i in range(len(self.list)):
            self.list[i].stop_engine()
        print("Tüm araçları durmakta!")

    def add_vehicle(self, vehicle):
        self.list.append(vehicle)

    def remove_vehicle(self, deleted_vehicle):
        self.list = [vehicle for vehicle in self.list if vehicle != deleted_vehicle]

    def list_vehicles(self):
        for v in self.list:
            print(v.__repr__())

    def list_running_vehicles(self):
        '''
        Şu an motoru çalışan araçları listeler.
        returns:
            çalışmakta olan araçların ismini/modelini döndürür.    

        '''
        running_vehicles = [veh.model for veh in self.list if veh.is_running == True]
        return running_vehicles

    def get_vehicle_by_id(self, search_id):
        '''Filo içinde ID’ye göre araç arayıp, aracı nesne halinde döndürür (yoksa None veya hata).'''
        for i in self.list:
            if (i.id == search_id):
                return i
            else:
                continue
        

    def count_by_type(self, vehicle_class):
        '''Belirli bir türden kaç tane araç olduğunu döndürür.'''
        pass


    def find_vehicle(self, keyword):
        '''
        İsme göre araç arama, örneğin “Toyota” geçenleri bul.
        returns:
            verilen keyworde göre bulunana araçları liste halinde döndürür.
        '''
        list=[]
        for i in self.list:
            if i.model.lower() == keyword.lower():
                list.append(i)
        return list


    def remove_all(self):
        '''Filodaki tüm araçları siler.'''
        self.list = []

    def sort_vehicles(self, by="id"):
        '''Araçları ID’ye veya tipine göre sıralar.'''
        self.list.sort(key=lambda v: getattr(v, by, None))
        for i in self.list:
            print(f"{i.model} | {i.id}")


f1 = FleetManager([t1, m1, c1])
f1.list_vehicles()

t2 = Truck("Mercedes - tır", 1002)
f1.add_vehicle(t2)
f1.add_vehicle(t3)
f1.list_vehicles()
f1.start_all()
f1.list_vehicles()

f1.sort_vehicles()
print(f1.find_vehicle("man"))

print(f1.get_vehicle_by_id(1001).model)
print(f1.get_vehicle_by_id(2001).model)
print(f1.get_vehicle_by_id(1003).model)

