frase = "fernando de noronha"

qtd_apareceu_mais = 0
letra_apareceu_mais = ''
i = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais < qtd_atual:
        qtd_apareceu_mais = qtd_atual
        letra_apareceu_mais = letra_atual

    i += 1

print(f"a letra que apareceu mais vezes foi: {letra_apareceu_mais}")
print(f"quantidade de vezes: {qtd_apareceu_mais}")
