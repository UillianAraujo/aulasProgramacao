# Condicionais
# if, elif e else
'''
E ae Uillian, bora dar saída hoje?
Se eu terminar a aula de Lógica de Programação, eu vou.
'''
#\/ Código \/
'''
trabalho_terminado = True
if trabalho_terminado == False:
    print('Beleze! Bons estudos!')
else:
    print('Opa! 
    Partiiiu...')
'''

'''
Ei, você consegue me ajudar a mover essas caixas lá pra fora hoje a tarde? 
Se eu estiver livre, sim. Mas, se não der, pede meu irmao para te judar.
'''

#\/ Código \/
'''
estou_livre = True
if estou_livre == True:
    print('Ok, posso te ajudar hoje sim!')
else:
    print('Estou ocupado hoje. Peça meu irmão para te ajudar.')
'''

'''
Desculpe, cheguei atrasado, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado no mês, então pode sim, caso contrário irá tomar suspesão.
'''
#\/ Código \/
'''
print('Desculpe, cheguei atrasado, ainda posso entrar?')

atrasos_mes = int(input('Quantas vezes chegou atrasado esse mês?'))
if atrasos_mes <= 2:
    print('Pode entrar.')
elif atrasos_mes == 3:
    print('Vá para secretária, vai tomar suspensão!')
else:
    print('Vou precisar conversar com seus responsáveis!')
'''
# Encontre o maior entre 2 números
'''
Pseudocódigo:
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
    print o primeiro valor é maior
else
    print o segundo valor é maior
'''

primeiro_valor = int(input('Digite o 1º valor: '))
segundo_valor = int(input('Digite o 2º valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior!')
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais!')
else:
    print('O segundo valor é maior!')
