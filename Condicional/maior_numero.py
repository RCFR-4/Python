# Faça um Programa que leia três números e mostre o maior deles#

n1 = float(input("entre com o 1 numero: "))
n2 = float(input("entre com o 2 numero: "))
n3 = float(input("entre com o 3 numero: "))

if (n1 > n2) and (n1 > n3):
    print(f"o maior numero é o {n1}")
elif (n2 > n1) and (n2 > n3):
    print(f"o maior numero é o {n2}")
else:
    print(f"o maior numero é o {n3}")
