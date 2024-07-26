largura = float(input("digite a largura do terreno: "))
comprimento = float(input("digite o comprimento do terreno: "))
valor = float(input("digite o valor metro quadrado: "))

area = largura * comprimento

preco = area * valor

print(f"area do terreno = {area:.2f}")
print(f"preço do terreno = {preco:.2f}")
