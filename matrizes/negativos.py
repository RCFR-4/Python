L = int(input("quantas linhas vai ter a matriz? "))
C = int(input("quantas colunas vai ter a matriz? "))


matriz = [[0 for x in range(C)] for x in range(L)]

quant = 0

for i in range(0, L):
    for j in range(0, C):
        matriz[i][j] = int(input(f"elemento [{i}, {j}]: "))

print()
print("valores negativos: ")
for i in range(0, L):
    for j in range(0, C):
        if matriz[i][j] < 0:
            print(f"{matriz[i][j]}")
