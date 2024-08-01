quant = 0
soma = 0
media = 0

print("digite as idades: ")
idade = int(input(""))

if idade < 0:
    print("impossivel calcular!")

while idade > 0:
    quant = quant + 1
    soma = soma + idade
    idade = int(input(""))
    media = soma / quant


if media > 0:
    print(f"MEDIA: {media:.2f}")
