def sum(a,b):
    return a+b

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b  

def div(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b  #what will be // instead of / ?