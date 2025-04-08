# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA E DESVIO DE PADRÃO, 
# DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 

import statistics

def calcular_moda(notas):
    return statistics.mode(notas)

def calcular_media(notas):
    return statistics.mean(notas)

def desvio_padrao(notas):
    return statistics.stdev(notas)

def maior_nota(notas):
    return max(notas)

def menor_nota(notas):
    return min(notas)

def exibir(notas):
    print (f'Moda das notas:{calcular_moda(notas)}')
    print (f'Média das notas:{calcular_media(notas):.2f}')
    print (f'Desvio de padrão:{desvio_padrao(notas):.2f}')
    print (f'Maior nota:{maior_nota(notas)}')
    print (f'Menor nota:{menor_nota(notas)}')

quantidade_notas = int(input('Quantas notas você deseja inserir? '))
notas = []

for i in range(quantidade_notas):
    nota = float(input('Digite a nota do aluno:'))
    notas.append(nota)

exibir(notas)
print ('-------'*2)


# Você é um analista de dados, e decidiu trocar de emprego. 
# Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você.
# Justificar por que decidiu por essa empresa. 
# Verifique isso através dos salários:

empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]

import statistics
media_empresa1 = statistics.mean(empresa1)
print (media_empresa1, 'de media da empresa 1.')
moda_empresa1 = statistics.mode(empresa1)
print (moda_empresa1, 'de moda da empresa 1')
mediana_empresa1 = statistics.median(empresa1)
print (mediana_empresa1, 'de médiana da empresa 1')
print ('-------'*2)

media_empresa2 = statistics.mean(empresa2)
print (media_empresa2, 'de media da empresa 2.')
moda_empresa2 = statistics.mode(empresa2)
print (moda_empresa2, 'de moda da empresa 2')
mediana_empresa2 = statistics.median(empresa2)
print (mediana_empresa2, 'de médiana da empresa 2')
print ('-------'*2)

media_empresa3 = statistics.mean(empresa3)
print (media_empresa3, 'de media da empresa 3.')
moda_empresa3 = statistics.mode(empresa3)
print (moda_empresa3, 'de moda da empresa 3')
mediana_empresa3 = statistics.median(empresa3)
print (mediana_empresa3, 'de médiana da empresa 3')
print ('-------'*2)

media_empresa4= statistics.mean(empresa4)
print (media_empresa4, 'de media da empresa 4.')
moda_empresa4 = statistics.mode(empresa4)
print (moda_empresa4, 'de moda da empresa 4')
mediana_empresa4 = statistics.median(empresa4)
print (mediana_empresa4, 'de médiana da empresa 4')