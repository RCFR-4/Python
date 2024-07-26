preco = float(input("entre com o preco unitario do produto: "))
quant = float(input("entre com a quantidade comprada: "))
dinheiro = float(input("dinheiro recebido: "))

total = preco * quant
troco = dinheiro - total

print(f"troco: {troco:.2f}")
