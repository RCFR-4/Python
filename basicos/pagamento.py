nome = input("nome do funcionario: ")
valor_hora = float(input("valor recebido por hora: "))
horas_trabalhadas = int(input("horas trabalhadas: "))

salario = valor_hora * horas_trabalhadas

print(f"{nome} deve receber {salario:.2f}")
