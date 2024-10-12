'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato'''

p1 = float(input("entre com o preco do primeiro produto: "))
p2 = float(input("entre com o preco do segundo produto: "))
p3 = float(input("entre com o preco do terceiro produto: "))

if (p1 < p2) and (p1 < p3):
    print("voçê deve comprar o primeiro produto, já que é o mais barato")
elif (p2 < p1) and (p2 < p3):
    print("voçê deve comprar o segundo produto, já que é o mais barato")
elif (p3 < p1) and (p3 < p2):
    print("voçê deve comprar o terceiro produto, já que é o mais barato")
else:
    print("qualquer um dos três produtos podem ser comprados, já que o valor é igual")
