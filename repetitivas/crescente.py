print("digite dois numeros: ")
x = int(input(""))
y = int(input(""))

if x > y:
    print("DECRESCENTE")
elif x < y:
    print("CRESCENTE")

while x != y:
    print("digite outro dois numeros: ")
    x = int(input(""))
    y = int(input(""))

    if x > y:
        print("DECRESCENTE")
    elif x < y:
        print("CRESCENTE")
