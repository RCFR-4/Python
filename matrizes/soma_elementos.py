ordem = int(input("qual a ordem da matriz? "))

matriz = [[0 for x in range(ordem)] for x in range(ordem)]

soma = 0

for i in range(0, ordem):
    for j in range(0, ordem):
        matriz[i][j] = int(input(f"elemento [{i}, {j}]: "))
        soma += matriz[i][j]

print()
print(f"soma dos valores da matriz: {soma}")
