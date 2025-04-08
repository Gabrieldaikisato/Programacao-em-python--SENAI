# match case
numero = 20 
match numero:
    case 0:
        print('É zero')
    case 1:
        print ('É um')
    case 2:
        print ('É dois')
    case _:
        print('Desconhecido')

# preciso verificar se o número é par
numero = int(input('Digite um número e veja se ele é par ou não.'))

match numero:
    case x if x % 2 == 0:
        print('O número é par.')
    case _:
        print('O número é ímpar')

# verificar se o número é positivo, negativo ou zero
number = int(input('Digite um número para descobrir se ele é positivo ou negativo:'))

match number:
    case 0:
        print('Esse número é zero!')
    case x if x > 0:
        print ('Número postivo!')
    case _:
        print('Número negativo!')

# verificar se uma string é vazia ou não

string = ""
match string:
    case "":
        print ('A string está vazia.')
    case _:
        print ('A string não está vazia.')

# verificar se o número é maior, menor ou igual a 10

n1 = float(input('Digite um número e veja se ele é maior ou menor que dez:'))
match n1:
    case x if x > 10:
        print('Número maior que dez!')
    case 10:
        print('Esse número é igual a 10!')
    case _:
        print('Esse número é menor que 10!')

# classificar uma idade em faixa etária - criança, jovem, adulto e idoso

faixa_etaria = int(input('Digite sua idade e veja sua faixa etária:'))
match faixa_etaria: 
    case x if x >= 1 and x <= 3:
        print('Bebê.')
    case x if x >= 4 and x < 13:
        print('Criança.')
    case x if x >= 14 and x < 18:
        print('Adolescente.')
    case x if x >= 18 and x < 60:
        print ('Adulto.')
    case _:
        print('Idoso')