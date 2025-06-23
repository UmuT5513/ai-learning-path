

def myfunction(myparameter:int) -> str:
    return str(myparameter)

def myfunction2(myparameter2:str) -> int:
    return int(myparameter2)

type(myfunction2(myfunction(10)))

# no issue (checked by mypy)

def dosth(param: list[str,float]) ->dict[str, int]:
    diction = {}
    for i in range(len(param)):
        diction[param[i]] = i
    return diction

print(dosth(["a", "b", "c",3.1,4.1,5.1]))