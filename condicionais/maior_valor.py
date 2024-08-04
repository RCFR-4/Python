valor1 = int(input("digite um valor: "))
valor2 = int(input("digite um outro valor: "))

if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor1 == valor2:
    print(f"os dois numeros são iguais")
else:
    print(f"{valor2} é maior que {valor1}")
