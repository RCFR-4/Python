'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input(
    "digite o turno que vc estuda: matutino(M) vespetino(V) noturno(N): ")

turno_m = turno.upper()

if turno_m == 'M':
    print("Boa Dia!")
elif turno_m == 'N':
    print("Boa Noite!")
elif turno_m == 'V':
    print("Boa Tarde!")
else:
    print("valor invalido!")
