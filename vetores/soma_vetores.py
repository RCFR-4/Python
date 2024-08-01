n = int(input("quantos valores vai ter cada vetor? "))

vetor1 = []
vetor2 = []
vetor3 = []

print("digite os valores do vetor a: ")
for i in range(0, n):
    numero = int(input(''))

    vetor1.append(numero)


print("digite os valores do vetor b: ")
for i in range(0, n):
    numero = int(input(''))

    vetor2.append(numero)


print("vetor resultante: ")
for i in range(0, n):
    soma = vetor1[i] + vetor2[i]
    vetor3.append(soma)

for valor in vetor3:
    print(valor)
