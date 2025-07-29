# NORMAL CLASS

class Investor:
    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash

    def __repr__(self):
        return f"Name: {self.name}"

    def __eq__(self, other):
        return self.cash == other.cash

    def __lt__(self, other):
        return self.cash < other.cash
    

i1 = Investor("Umut", 23, 10000000)
i2 = Investor("Man", 56,  50000000)

print(i1 < i2) #true
print(i1==i2) # false



# DATA CLASSES
from dataclasses import dataclass, field

@dataclass
class Investor:
    name: str
    age:int
    cash:float
# no constructor, no __repr__ method

i1 = Investor("jon", 80, 700)
i2 = Investor("mkie", 18, 1000)
i3 = Investor("mkie", 38, 4000)

print(i2) #Investor(name='mkie', age=18)
print(i1==i2) # false (obj olarak farklı lar)




# DATA CLASSES --> FIELD()
@dataclass
class Investor:
    name: str
    age:int
    cash:float = field(repr=False) # cash will not be included

i1 = Investor(name="jon", age=80, cash=700)
print(i1)



# DATA CLASSES --> INIT FALSE
@dataclass
class Investor:
    name: str
    age:int
    cash:float = field(init=False)

i1 = Investor(name="me", age=80) #cash i başlatmaya gerek yok 





# DATA CLASSES --> ORDER TRUE
@dataclass(order=True)
class Investor:
    sorted_index: float = field(init=False, repr=False)
    name: str
    age:int
    cash:float

    def __post_init__(self):
        self.sorted_index = self.cash

i1 = Investor(name="jon", age=80, cash=400)
i2 = Investor(name="cris", age=10, cash=100)
print(i1 > i2) # true
i3 = Investor(name="clay", age=40, cash=1000)
i4 = Investor(name="man", age=50, cash=700)
i5 = Investor(name="bob", age=30, cash=800)

my_list= [i1, i2, i3, i4, i5]
my_list.sort()
print(my_list)

# unsafe_hash TRUE and frozen TRUE --> hashable, mutable
