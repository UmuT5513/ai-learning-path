import time

def timer(fn):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = fn(*args,**kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{fn.__name__} fonksiyonu {elapsed_time} sürdü.")
        return result
    return wrapper

def error_logger(fn):
    def wrapper(*args,**kwargs):
        try:
            return fn(*args,**kwargs)
        except Exception as ex:
            print(f"Hata: {fn.__name__} fonksiyonunda hata oluştu: {ex}")
    return wrapper

# @error_logger
# @timer
# def bolme(x,y):
#     time.sleep(1)
#     return x/y

# bolme(10,2)
# bolme(10,0)

def fibonacci_inner(n):
    """n'inci fibonacci sayısını döndürür."""
    if n < 0:
        raise ValueError("n negatif olamaz!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_inner(n-1) + fibonacci_inner(n-2)

@error_logger
@timer
def fibonacci(n):
    '''n'inci fibonacci sayısını döndürür.'''
    time.sleep(0.5)
    return fibonacci_inner(n)



# Doğru kullanım
print(fibonacci(10))  # 10. fibonacci sayısı

# Hatalı kullanım
fibonacci(-2) # Negatif değer ile çağrıldığında hata verecek