def error_logger(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args,**kwargs)
        except Exception as ex:
            print(f"{fn.__name__} fonksiyonunda bir hata: {ex}")
    return wrapper

def bolme(x,y):
    return x/y

sonuc = error_logger(bolme)
sonuc(10,0)


