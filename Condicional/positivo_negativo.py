# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo#

v = float(input("entre com um valor: "))

if v < 0:
    print(f"o valor digitado {v} é negativo!")
elif v > 0:
    print(f"o valor digitado {v} é positivo!")
else:
    print(f"o valor digitado {v} é neutro!")
