''' Faça um programa que receba dois números inteiros e gere os números inteiros que estão 
no intervalo compreendido por eles '''

n1 = int(input("entre com o primeiro numero inteiro: "))
n2 = int(input("entre com o segundo numero inteiro: "))

for n1 in range(n1+1, n2):
    print(n1)
