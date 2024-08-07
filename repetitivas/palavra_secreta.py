secreta = 'game'
tentativas = 0
palavra_adivinhada = ['*' for _ in secreta]

while tentativas < len(secreta) * 2:

    letra_usuario = input(
        f"digite uma letra que vc acha que faz parte da palavra secreta (apenas {len(secreta) * 2} tentativas): ")

    while len(letra_usuario) != 1:
        letra_usuario = input("por favor, digite apenas uma letra: ")

    if letra_usuario in secreta:
        for i in range(len(secreta)):
            if letra_usuario == secreta[i]:
                palavra_adivinhada[i] = letra_usuario
        print(''.join(palavra_adivinhada))
    else:
        print("letra incorreta")

    tentativas += 1

    if '*' not in palavra_adivinhada:
        print("parabens! vc acertou a palavra secreta!")
        break


if '*' in palavra_adivinhada:
    print(
        f"infelizmente vc não conseguiu acertar nas tentativas combinadas. a palavra secreta é {secreta}")
