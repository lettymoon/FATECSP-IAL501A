#Estrutura sequencial
#índice de massa corporal (IMC)

#Crie uma função para ler o peso e a altura de uma pessoa e exibir seu IMC


def imc():
    p = float(input('Peso? '))
    a = float(input('Altura? '))
    i = p/(a**2)
    print('IMC: %.2f' % i)