# Faça um programa que leia 5 números e informe o maior número #

maior = float('-inf')

print("insira 5 numeros: ")
for i in range(1, 6):
    n = int(input(f"{i} numero: "))

    if n > maior:
        maior = n

print(f"o maior numero digitado foi: {maior}")
