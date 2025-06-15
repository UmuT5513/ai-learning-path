def filter(func, liste):
    result = []
    for item in liste:
        if func(item):
            result.append(item)
    return result
    
def is_even(sayi):
    return sayi % 2 == 0

def is_positive(sayi):
    return sayi > 0

list = [1,2,3,-4,2,6,10,7,-4,0]

print(filter(is_even, list))
print(filter(is_positive, list))