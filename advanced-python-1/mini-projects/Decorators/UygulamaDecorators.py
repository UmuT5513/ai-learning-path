# decorator ile generator ve liste nin hızlarının karşılaştırılması

def speed(fn):
    import time
    def inner():
        print(f"{fn.__name__} metodu çalışıyor.")
        fn_start_time = time.time()
        result = fn()
        fn_run_time = time.time() - fn_start_time
        print(f"geçen süre {fn_run_time}")
        return result
    return inner

def sum_gen():
    return sum((x for x in range(10000000)))

@speed
def sum_list():
    return sum([x for x in range(10000000)])


sonuc = speed(sum_gen)
sonuc()
sum_list()
