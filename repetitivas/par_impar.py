n = int(input("quantos numeros vc vai digitar? "))

for i in range(0, n):
    numero = int(input("digite um numero: "))

    if (numero % 2 == 0) and (numero > 0):
        print("par positivo")
    elif (numero % 2 == 0) and (numero < 0):
        print("par negativo")
    elif (numero % 2 != 0) and (numero > 0):
        print("impar positivo")
    elif (numero % 2 != 0) and (numero < 0):
        print("impar negativo")
    else:
        print("nulo")
