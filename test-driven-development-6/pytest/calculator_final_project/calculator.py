def check_input(operation):
    '''parametre olarak gelen operation un sonucunda elde edilen sayıyı döndürür.'''
    def wrapper(*args, **kwargs):
        try:
            return operation(*args, **kwargs)
        except TypeError as e:
            print(f"Int ya da Float bir değer girin! {e}")
            raise e
        except ZeroDivisionError as e:
            print(f"{operation.__name__} işleminde payda 0 olamaz! {e}")
            raise e
    return wrapper

@check_input
def topla(x,y):
    return x+y

@check_input
def carp(x,y):
    return x*y

@check_input
def bol(x,y):
    return x/y

@check_input
def cikar(x,y):
    return x-y