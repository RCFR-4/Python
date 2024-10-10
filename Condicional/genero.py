'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino,
Sexo Inválido'''

genero = input("insira seu genero feminino[F] masculino[M]: ")

if (genero == 'f') or (genero == 'F'):
    print(f"o seu genero é feminino")
elif (genero == 'm') or (genero == 'M'):
    print(f"o seu genero é masculino")
else:
    print("genero invalido")
