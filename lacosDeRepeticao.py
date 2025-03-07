# Laços de Repetição

for palavra in range(1,4):
    print('Carregando')

'''
for item in coleção:
    espressão
'''
for item in range(1,20): 
    print(item)
for item in range(1,20 + 1): # +1 é para adicinar ao final da contagem
    print(item)
for item in range(0,21,5): # o 5 determina qe será contato 5 em 5
    print(item)


animaisTerrestres = ['Cobra', 'Vaca', 'Leão','Lobo','Urso']
for animal in animaisTerrestres:
    print(animal)

animaisTerrestres = ['Cobra', 'Vaca', 'Leão','Lobo','Urso']
for animal in animaisTerrestres:
    print(animaisTerrestres)

# Problema de 1 a N - imprema os valores de 1 a N
'''
input numero maximo
valor inicial = 1
loop de valorInical a numero_maximo
    print valor
'''
valorMaximo = int(input('Digite o valor máximo: '))
valorInicial = 1
for numero in range(valorInicial, valorMaximo + 1):
    print(numero)

