'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido'''

n = int(input("insira a nota entre zero e dez (apenas numeros inteiros): "))

while (n < 0) or (n > 10):
    n = int(input("valor invalido. insire novamente: "))

print(f"valor digitado: {n}")
