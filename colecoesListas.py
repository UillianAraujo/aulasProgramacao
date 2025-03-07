'''
# Some os valores
dados de uma colecao de dados "idade" [15, 87, 32, 65, 56, 32, 49, 37],
imprima na tela a soma destes valores

idade = [15, 87, 32, 65, 56, 32, 49, 37]
soma = 0
loop idade em idades 
    soma = soma + idade
imprima  soma

'''

# Solução

idades = [15, 87, 32, 65, 56, 32, 49, 37]
soma = 0
for idade in idades:
    soma = soma + idade
print(soma)
# Resultado: 373