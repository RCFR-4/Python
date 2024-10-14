# Faça um programa que leia 5 números e informe a media #

soma = 0
quantidade = 0
media = 0

print("insira 5 numeros: ")
for i in range(1, 6):
    n = int(input(f"{i} numero: "))

    soma += n
    quantidade += 1

print(f"a media dos numeros digitados é: {soma / quantidade}")
