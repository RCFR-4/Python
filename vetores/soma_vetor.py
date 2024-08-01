n = int(input("quantos numeros vc vai digitar? "))

vetor = []

for i in range(0, n):
    numero = float(input("digite o numero: "))
    vetor.append(numero)

soma = sum(vetor)
media = soma / n

print()
print("valores: ", end=' ')
for numero in vetor:
    print(f"{numero} ", end=' ')


print(f"\nsoma: {soma}")
print(f"media: {media}")
