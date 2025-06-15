
#1
def dec_selamlama(call_count):
    def selamlama(fn):
        def inner(ad):
            for _ in range(call_count):
                fn(ad)
        return inner
    return selamlama

@dec_selamlama(call_count=2)
def guno(ad):
    print(f"günaydın benim adım {ad}")
    
@dec_selamlama(call_count=3)
def iyigunler(ad):
    print(f"iyi günler benim adım {ad}")

guno("umut")
iyigunler("memet")


#2

def dec_speed(count):
    def speed(fn):
        import time
        def inner():
            print(f"{fn.__name__} metodu çalışıyor.")
            for _ in range(count):
                fn_start_time = time.time()
                result = fn()
                fn_run_time = time.time() - fn_start_time
                print(f"geçen süre {fn_run_time}")
            return result
        return inner
    return speed

@dec_speed(count=3)
def sum_gen():
    return sum((x for x in range(100000000)))

@dec_speed(count=3)
def sum_list():
    return sum([x for x in range(100000000)])

sum_gen()
sum_list()
