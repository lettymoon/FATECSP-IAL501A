#Análise de correção formal

def resto(a,b):
    r = a
    while r >= b:
        r -= b
    return r


print(resto(10,5))