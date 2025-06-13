# “Limit’e kadar çift sayıların akışını yöneten iterable sınıf.”

class EvenFlow:
    def __init__(self,limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.limit:
            x = self.current
            self.current += 2
            return x
        else:
            raise StopIteration


for even in EvenFlow(10):
    print(even)