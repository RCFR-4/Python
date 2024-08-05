hora = int(input("qual é o horario atual (0-23)? "))

if 0 <= hora <= 23:
    if hora <= 11:
        print("bom dia!")
    elif hora <= 17:
        print("boa tarde!")
    else:
        print("boa noite!")
else:
    print("horario invalido!")
