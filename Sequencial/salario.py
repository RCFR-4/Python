'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês'''

ganha_hora = float(input("qual o seu ganho por hora no seu emprego? "))
horas_mes = int(input("qual a sua quantidade de horas trabalhadas por mês? "))

salario = ganha_hora * horas_mes

print(f"o seu salario no mês inserido é: {salario}")
