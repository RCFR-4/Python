# Faça um programa que leia 5 números e informe a soma total entre eles #

soma = 0

print("insira 5 numeros: ")
for i in range(1, 6):
    n = int(input(f"{i} numero: "))

    soma += n

print(f"a soma total dos numeros digitado é: {soma}")
