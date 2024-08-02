ordem = int(input("ordem da matriz: "))

matriz = [[0 for x in range(ordem)] for x in range(ordem)]

quant = 0

for i in range(0, ordem):
    for j in range(0, ordem):
        matriz[i][j] = int(input(f"elemento [{i}, {j}]: "))
        if matriz[i][j] < 0:
            quant += 1

print()
print("diagonal principal: ")
for i in range(0, ordem):
    for j in range(0, ordem):
        if i == j:
            print(f"{matriz[i][j]} ", end=" ")

print()
print(f"quantidade de negativos: {quant}")
