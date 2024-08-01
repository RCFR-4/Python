n1 = int(input("primeiro valor: "))
n2 = int(input("segundo valor: "))
n3 = int(input("terceiro valor: "))

if (n1 < n2) and (n1 < n3):
    print(f"MENOR VALOR: {n1}")
elif (n2 < n1) and (n2 < n3):
    print(f"MENOR VALOR: {n2}")
else:
    print(f"MENOR VALOR: {n3}")
