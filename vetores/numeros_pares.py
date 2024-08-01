n = int(input("quantos numeros vc vai digitar? "))

pares = []

quant = 0
for i in range(0, n):
    numero = int(input("digite um numero: "))

    if numero % 2 == 0:
        pares.append(numero)
        quant = quant + 1


print()
print("numeros pares: ")
for numero in pares:
    print(f"{numero}", end=' ')

print()
print(f"\nquantidade de pares: {quant}")
