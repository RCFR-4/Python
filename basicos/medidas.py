A = float(input("digite a medida A: "))
B = float(input("digite a medida B: "))
C = float(input("digite a medida C: "))

area_quadrado = A * A
area_triangulo = (A * B) / 2
area_trapezio = ((A + B) * C) / 2

print(f"AREA DO QUADRADO: {area_quadrado:.4f}")
print(f"AREA DO TRIANGULO: {area_triangulo:.4f}")
print(f"AREA DO TRAPEZIO: {area_trapezio:.4f}")
