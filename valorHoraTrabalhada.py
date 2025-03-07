# Como variáveis seriam usadas em um programa real?
# Problema 1 - Valor por hora
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input('Qual é so seu salário mensal?')

horas_trabalhadas_por_dia = input('Quantas horas trabalha por dia?')

dias_na_semana = input('Quantos dias trabalha na semana?')

semanas_mes = 4

horas_trabalhadas_por_mes = int(horas_trabalhadas_por_dia) * int(dias_na_semana) * semanas_mes

valor_hora_mes = int(salario_mensal) / int(horas_trabalhadas_por_mes)

print('O valor/hora trabalhada é:') 
print(valor_hora_mes)



nota_um = int(input('1ª nota: '))
nota_dois = int(input('2ª nota: '))
nota_tres = int(input('3ª nota: '))
nota_quatro = int(input('4ª nota: '))
soma_das_notas = (nota_um + nota_dois + nota_tres + nota_quatro)
media_das_notas = (soma_das_notas) / 4
print('Sua mádia é: ')
print(media_das_notas)