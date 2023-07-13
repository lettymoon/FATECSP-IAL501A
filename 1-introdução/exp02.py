#análise de correção empírica

def resto(a,b):
    r = a
    while r > b:
        r -= b
    return r

print(resto(19,5))