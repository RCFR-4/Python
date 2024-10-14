'''
. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';

'''

nome = ''
idade = 0
salario = 0
sexo = ''
E_civil = ''

nome = input("digite o nome (minimo mais que 3 caracteres): ")
while len(nome) <= 3:
    nome = input(
        "menos caracteres do que a quantidade permitida. insira novamente: ")


idade = int(input("digite a idade (0 a 150): "))
while (idade < 0) or (idade > 150):
    idade = int(input("digite uma idade valida. insira novamente: "))


salario = float(input("digite o salario (minimo maior que zero): "))
while salario <= 0:
    salario = float(
        input("o salario digitado deve ser maior que zero. insira novamente: "))


sexo = input("digite o seu sexo feminino(f) masculino(m): ").lower()
while sexo not in ['f', 'm']:
    sexo = input("valor invalido. insira novamente: ").lower()


E_civil = input(
    "digite a sua situação civil casado(c) solteiro(s) divorciado(d) viuvo(v): ").lower()
while E_civil not in ['c', 's', 'd', 'v']:
    E_civil = input(
        "menos caracteres do que a quantidade permitida. insira novamente: ").lower()

print("\ninformações inseridas:")
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"salario: {salario}")
print(f"sexo: {sexo}")
print(f"estado civil: {E_civil}")
