# Faça um Programa que leia três números e mostre o maior e o menor deles#

n1 = int(input("entre com o 1 numero: "))
n2 = int(input("entre com o 2 numero: "))
n3 = int(input("entre com o 3 numero: "))


menor = 0
maior = 0


if (n1 < n2) and (n1 < n3):
    menor = n1
elif (n2 < n1) and (n2 < n3):
    menor = n2
else:
    menor = n3


if (n1 > n2) and (n1 > n3):
    maior = n1
elif (n2 > n1) and (n2 > n3):
    maior = n2
else:
    maior = n3

print(f"o maior numero entre os digitados é o {maior}. já o menor é {menor}")
