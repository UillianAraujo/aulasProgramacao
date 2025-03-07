'''
crie um programa que recebe um numero e imprime o seu fatorial.
#metodo 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(tente explicar este problema para voce mesmoem  voz alta e peca mais informacoes/investigue mais até voce compreender completamente o problema.)

1. quais sao os dados de entrada necessario?
    - um numero inteiro
2. oque devo fazer comestes dados?
    - calcular o fatorial do numero
3. quais sao as restricoes do problema?
    - o numero deve ser inteiro
    - o numero deve ser positivo
4. quais sao as saidas(resultado) do problema?
    - o resultado esperado é que o fatorial do numero providenciado seja exibido
5. como devo chegar ao resultado?
    input numero
    if numero > 0
    if numero == inteiro
    fatorial = 1
    loop de 1 a numero
    fatorial = fatorial * numero
    print(fatorial)
'''

numero = int(input('Digite um numero: '))
if numero >= 0:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print(fatorial)
else:
    print('O numero deve ser inteiro')
