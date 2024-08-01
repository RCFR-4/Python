n = int(input("quantas pessoas serão digitadas? "))

idades = []
nomes = []
alturas = []
menor = []

for i in range(0, n):
    print(f"dados da {i+1} pessoa: ")
    nome = input("nome: ")
    idade = int(input("idade: "))
    altura = float(input("altura: "))

    nomes.append(nome)
    alturas.append(altura)
    idades.append(idade)

    if idade < 16:
        menor.append(nome)

altura_media = sum(alturas) / n

porcentagem = ((len(menor) / n) * 100)

print()
print(f"altura media: {altura_media:.2f}")
print(f"porcentagem de menores de 16 anos: {porcentagem:.1f}")

for nome in menor:
    print(nome)
