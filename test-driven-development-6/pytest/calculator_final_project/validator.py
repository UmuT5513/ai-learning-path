# TODO: test ile birlikte doldurulacak

def is_valid_number(x):
    if type(x) in [int, float]:
        return True
    else:
        return False
    

def can_perform(operation:str, role:str)->bool:
    if role == "user":
        if operation in ["topla", "cikar"]:
            return True 
        else: 
            return False

    if role == "admin":
        return True     

    return False #farklı roller   