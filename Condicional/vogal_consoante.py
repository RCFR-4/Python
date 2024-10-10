# Faça um Programa que verifique se uma letra digitada é vogal ou consoante#

letra = input("digite apenas uma letra: ")

letra_maiscula = letra.upper()

if (letra_maiscula == 'A') or (letra_maiscula == 'U') or (letra_maiscula == 'I') or (letra_maiscula == 'E') or (letra_maiscula == 'O'):
    print(f"a letra digitada {letra_maiscula} é uma vogal!")
else:
    print(f"a letra digitada {letra_maiscula} é uma consoante!")
