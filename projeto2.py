'''
Escreva um programa que ao inicar, gere um valor eleatório entre 1 e 10 e permite que o usuário chute um número até que o valor aleatório gerado no inicio do porograma 
seja chutado corretamente.
O programa deve informar se o chute foi maioro, menor ou igaul que o valor aleatório gerado.


# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo  em voz alta e peca mais informacoes/investigue mais até compreender completamente o problema.)

1. quais sao os dados de entreda necessários?   
    valor aleatório de 1 a 10
    chute do usuário
2. oque devo fazer com estes dados?
    devo comparar o chuve do usário com o valor aleatório gerado no inicio do programa e 
dizer se o chute é maior, menor ou igual ao valor gerado no inicio do programa.
3. quais são as restricoes deste problema?
    o programa deve permitir que o usuário chute um número até que o valor aleatório gerado no inicio do porograma
seja chutado corretamente.
4. qual é o resultado esperado?
    o programa deve informar se o chute foi maior, menor ou igual que o valor aleatório gerado.
5. qual é a seguerncia de passos a ser feita para resolver este problema?
    1. gerar um valor aleatório entre 1 e 10
    2. permitir que o usuário chute um número
    3. comparar o chute do usuário com o valor aleatório gerado no inicio do programa
    4. informar se o chute foi maior, menor ou igual ao valor aleatório gerado
    5. se o chute for igual ao valor aleatório gerado, encerrar o programa
    6. se o chute for diferente do valor aleatório gerado, permitir que o usuário chute novamente
    7. repetir os passos 3, 4, 5 e 6 até que o chute do usuário seja igual ao valor aleatório gerado no inicio do programa
    8. encerrar o programa

'''

import random

valorAleatório = random.randint(1, 10)

acertou = False
while acertou == False:
    chute = int(input("Chute um número entre 1 e 10: "))
    if chute > valorAleatório:
        print("Chute um número menor!")
    elif chute < valorAleatório:
        print("Chute um número maior!")
    else:
        acertou = True
        print("Parabéns! Você acertou o número!")