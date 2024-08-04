nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

if nome != '' or idade != '':
    print(f"seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print("seu nome contem espaço")
    else:
        print("seu nome não contem espaço")

    print(f"seu nome contem {len(nome)} letras")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a ultima letra do seu nome é {nome[-1]}")
else:
    print("desculpe, vc deixou campos vazios")
