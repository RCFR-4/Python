l = int(input("numero de linhas: "))
c = int(input("numero de colunas: "))

matriz = [[0 for x in range(c)] for x in range(l)]

for i in range(0, l):
    for j in range(0, c):
        matriz[i][j] = int(input(f"elemento [{i}, {j}]: "))

print()
print("matriz digitada: ")
for i in range(0, l):
    for j in range(0, c):
        print(f"{matriz[i][j]} ", end=" ")
    print()
