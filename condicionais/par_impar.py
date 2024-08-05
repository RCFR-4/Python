try:
    n = int(input("digite um numero inteiro: "))

    if n % 2 == 0:
        print("o numero digitado é par!")
    else:
        print("o numero digitado é impar!")

except ValueError:
    print("o valor digitado não é inteiro")
