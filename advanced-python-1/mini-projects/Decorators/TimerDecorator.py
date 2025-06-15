import time

def timer(fn):
    def inner(*args, **kargs):
        start_time = time.time()
        result = fn(*args, **kargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{fn.__name__} fonksiyonu {elapsed_time:.4f} saniye sürdü.")
        return result
    return inner

@timer
def bekle(second=1):
    time.sleep(second)
    print("bekleme bitti.")

bekle(second=4)
bekle(second=2)
bekle()
