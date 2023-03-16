def f(n):
    
    i = n // 2
    while i < 2*n: i = i + i // 2
    return 2*i

n = int(input("Escolha um número: "))
print(f(n))
