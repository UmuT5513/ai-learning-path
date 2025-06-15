class FiboFlow:
    """
    Fibonacci sayılarını üreten bir iterator sınıfı.
    Başlangıç değerleri ve üretilecek eleman sayısı verilebilir.
    """

    def __init__(self, start, count=10):
        """
        FiboFlow nesnesini başlatır.

        Args:
            start (tuple): Fibonacci dizisinin ilk iki elemanı (a, b).
            count (int, optional): Üretilecek Fibonacci sayısı adedi. Varsayılan 10.
        """
        self.count = count
        self.a = start[0]
        self.b = start[1]


    def __iter__(self):
        """
        Iterator nesnesini döndürür.

        Returns:
            self: Iterator nesnesi.
        """
        return self
    
    def __next__(self):
        """
        Bir sonraki Fibonacci sayısını döndürür.

        Returns:
            int: Bir sonraki Fibonacci sayısı.

        Raises:
            StopIteration: Üretilecek sayı kalmadığında fırlatılır.
        """
        if self.count >= 0:
            x = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count -= 1
            return x
        else:
            raise StopIteration
        

for fib in FiboFlow(start=(5,10), count=10):
    print(fib)