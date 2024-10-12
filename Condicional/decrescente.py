# Faça um Programa que leia três números e mostre-os em ordem decrescente.#

n1 = int(input("entre com o primeiro numero: "))
n2 = int(input("entre com o segundo numero: "))
n3 = int(input("entre com o terceiro numero: "))

maior = 0
meio = 0
menor = 0

if (n1 < n2) and (n1 < n3):
    menor = n1
elif (n1 > n2) and (n1 > n3):
    maior = n1
else:
    meio = n1


if (n2 < n1) and (n2 < n3):
    menor = n2
elif (n2 > n1) and (n2 > n3):
    maior = n2
else:
    meio = n2


if (n3 < n2) and (n3 < n1):
    menor = n3
elif (n3 > n2) and (n3 > n1):
    maior = n3
else:
    meio = n3

print(f"os numeros digitados em ordem decrescente: {maior} {meio} {menor}")
