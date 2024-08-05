nome = input("entre com seu primeiro nome: ")

if len(nome) <= 4:
    print("seu nome é curto!")
elif len(nome) <= 6:
    print("seu nome é normal!")
else:
    print("seu nome é muito grande!")
