#Peça para o usuário digitar um número, verifique se um número é positivo,negativo ou zero.
numero = float(input('Digite um número para ver se é positivo, negativo ou zero:'))
if numero == 0:
     print ('O número é zero!')
elif numero > 0:
    print ('O número é postivo!')
else:
     print ('O número é negativo!')
    
#  Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.
idade = int(input('Digite sua idade:'))
if idade >= 18:
     print ('Você já pode votar!')
else: 
     print ('Você não tem idade suficiente para votar.')


#  Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
number = float(input('Digite um número e veja se é impar ou par'))
if number % 2 ==0:
     print(f"O número {number} é par.")
else:
     print(f"O número {number} é impar.")


# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno
lado1 = float(input('Digite o primeiro lado do triângulo:'))
lado2 = float(input('Digite o segundo lado do triângulo:'))
lado3 = float(input('Digite o terceiro lado do triângulo:'))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print('Os lados devem ser maiores que zero para formar um triângulo.')
else:
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
       
        if lado1 == lado2 == lado3:
            print('O triângulo é equilátero!')
        elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
            print('O triângulo é isósceles!')
        else:
            print('O triângulo é escaleno!')
    else:
        print('Os lados não formam um triângulo!')


# Determine se um número é múltiplo de 5 e 7.
n = float(input('Digite um número para verificar se ele é múltiplo de 5 e 7:'))
if n % 5 == 0 and n % 7 == 0:
    print ('Esse número é múltiplo!')
else: 
    print ('Esse número não é múltiplo!')


# Verifique se um número é positivo e maior que 10
n1 = float(input('Digite um número para ver se ele é positivo e maior que 10:'))
if n1 > 0 and n1 > 10:
    print ('Esse número é positivo e maior que dez!')
elif n1 > 0 and n1 <= 10:
    print ('Esse número é positivo porém menor que dez!')
else:
    print ('Esse número é negativo e menor que dez!')



# Verifique se um número é divisível por 3 ou 5. 
n2 = float(input('Digite um número e vamos descobrir se ele é divisível por 3 ou por 5:'))
if n2 % 3 == 0 and n2 % 5 == 0:
     print ('O número é divisível por 3 e por 5!')
elif n2 % 5 == 0:
    print ('O número é divisível por 5!')
elif n2 % 3 == 0:
    print ('O número é divisível por 3!')
else:
    print('O número não é divisível por nenhum dos dois.')