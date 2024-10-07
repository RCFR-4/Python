# Faça um Programa que peça dois números e imprima o maior deles.#

n1 = int(input("entre com o primeiro numero: "))
n2 = int(input("entre com o segundo numero: "))

if n1 > n2:
    print(f"o maior numero é: {n1}")
elif n1 < n2:
    print(f"o maior numero é: {n2}")
else:
    print(f"os dois numeros são iguais")
