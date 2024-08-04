n = int(input("quantos numeros vc vai digitar? "))

vetor = []

for i in range(0, n):
    numero = int(input("digite um numero: "))
    vetor.append(numero)

print("valores negativos")

for numero in vetor:
    if numero < 0:
        print(numero)
