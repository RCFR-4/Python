'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9)'''


f = float(input(
    "entre com a temperatura em fahrenheit que deseja converter pra celsius: "))

c = 5 * ((f - 32) / 9)

print(f"a temperatura insirida convertida em celsius é aproximadamente {
      c:.0f} graus")
