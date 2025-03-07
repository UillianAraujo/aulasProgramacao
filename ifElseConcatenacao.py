'''nome = input(str('Nome: '))
sobrenome = input(str('Sobrenome: '))
print('Seja bem-vindo: ' + sobrenome + ', ' + nome)
'''
#-------------------------------------------------------
nome = str(input('Qual seu nome? '))
sobrenome = str(input('Qual sobrenome? '))
print('Agora informe suas notas bimestreais!')
nota1 = int(input('Nota do primeio bimestres: '))
nota2 = int(input('Nota do segundo bimestre: '))
nota3 = int(input('Nota do terceiro bimestre: '))
nota4 = int(input('Nota do quarto bimestre: '))
media_notas = (nota1 + nota2 + nota3 + nota4) / 4
if media_notas >= 6:
    print('PARABÉNS ' , nome , ' ' , sobrenome , ', você passou de ano!')
   
else:
    print(nome + ' ' + sobrenome + ' você está REPROVADO!')
