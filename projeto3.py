'''
Crie um programa qwue recebe do usuário um valor que represtenta a velocidade e com base nessa velocidade 
diga se ela tomou uma multa leve, grave ou gravíssima. Levando em consideraçao que a pessoa estiver 
abaiaxo da velocidade máxima o programa deve exibir "não houve multa", caso esteja até 10 km acima, exibir: 
"multa leve", caso esteja entre 11 e 20 km acima, exibir: "multa grave" e caso esteja acima de 20 km exibir:
"multa gravíssima".

'''

velocidade = float(input("Digite a velocidade do veículo: "))
velocidadeMaxima = 80

if velocidade <= velocidadeMaxima:
    print("Não houve aplicação de multa")
elif velocidade > velocidadeMaxima and velocidade <= velocidadeMaxima + 10:
    print("Multa leve")
elif velocidade > velocidadeMaxima + 11 and velocidade <= velocidadeMaxima + 20:
    print("Multa grave")
else:
    print("Multa gravíssima")