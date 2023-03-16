#Crie a função recursiva bits(n) que devolve a quantidade de bits
#necessários para representar o número natural n em binário.

def bits(n):

    if n < 2: return 1
    return bits(n//2) + 1

n = int(input("Escolha um número para devolver a quantidade de bits necessários para representar o número em binário: "))
print(bits(n))