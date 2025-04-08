
# 1 - Crie um número aleatório de 5,10
import random

def numero_aleatorio():
 numero_aleatorio = random.randint(5,10)
 print (numero_aleatorio)

print ("-"*12)

# 2 - Crie 3 números aleatórios
def numero_aleatorio2():
    n2_aleatorio = random.randint (1,101)
    n3_aleatorio = random.randint (1,101)
    n4_aleatorio = random.randint (1,101)
    print (n2_aleatorio, n3_aleatorio, n4_aleatorio)

# 3 - Crie um número aleatório entre 10 a 30 utilize o range()
def numero_aleatorio3():
    number = range(10,31)
    random_number = random.choice(number)
    print(random_number)


# 4 - Contagem regressiva simples
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".
def contagem_regressiva():
    for u in range (10,0,-1):
        print (u)
    print('Fogo!')


# 5 - Soma de números pares
# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
def soma_par():
    numero_inteiro = int(input('Digite um número inteiro e positivo:'))
    if numero_inteiro <= 0:
     print('Esse número não é positvo')
    else:
     soma = 0
     for i in range(2, numero_inteiro +1, 2):
        soma += i
     print(f"A soma de todos os números pares de 2 até {numero_inteiro} é: {soma}")

# 6 - Tabuada de multiplicação
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
def tabuada():
    tabuada = int(input('Insira um número e veja a tabuada dele:'))
    for i in range (1,11):
        resultado = tabuada * i
        print (f'{tabuada} x {i} = {resultado}')

# 7 -  Números ímpares reversos
# Exiba uma contagem regressiva de números ímpares de 99 a 1.
def contagem_regressiva2():
    for i in range (99,0, -2):
     print (i)

# CHAMAR TODAS ELAS PARA UM ARQUIVO MAIN()