class PrimeQuest:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2
        self.primes = []

    def is_prime(self, num):
        return all(num % p != 0 for p in self.primes if p * p <= num) #n sayısının asallığını kontrol etmek için 2’den √n’e kadar bölme denemesi yapmak
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.limit:
            n = self.current
            self.current += 1
            if self.is_prime(n):
                self.primes.append(n)
                return n
        raise StopIteration
    

for prime in PrimeQuest(50):
    print(prime)
    
