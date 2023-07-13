#Assenção

def resto(a,b):
    assert a <= 0 and b < 0
    r = a
    while r >= b:
        r -= b
    return r


print(resto(10,5))