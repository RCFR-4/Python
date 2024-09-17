# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.#

compri = float(input("insira o comprimento de um dos lados do quadrado: "))

area = compri * compri
dobro_area = area * 2

print(f"o dobro da area do quadrado é {dobro_area:.2f}")
