try:
    continuar = 0
    while continuar != 6:
        n1 = float(input("entre com o primeiro valor: "))
        n2 = float(input("entre com o segundo valor: "))

        continuar = float(input(
            "qual será a operação utilizada? adição(1) subtração(2) multiplicação(3) divisão(4): "))

        if continuar == 1:
            print(f"resultado da adição: {n1 + n2}")
        elif continuar == 2:
            print(f"resultado da subtração: {n1 - n2}")
        elif continuar == 3:
            print(f"resultado da multiplicação: {n1 * n2}")
        elif continuar == 4:
            if n2 != 0:
                print(f"resultado da divisão: {n1 / n2}")
            else:
                print("não é possivel dividir por 0")

        continuar = int(input("deseja fazer outra operação? sim(5) não(6): "))
except ValueError:
    print("por favor, digite um numero valido")
