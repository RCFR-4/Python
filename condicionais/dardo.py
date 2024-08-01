distancia1 = float(input("digite as três distancias: "))
distancia2 = float(input(""))
distancia3 = float(input(""))

if (distancia1 > distancia2) and (distancia1 > distancia3):
    print(f"maior distancia: {distancia1}")
elif (distancia2 > distancia1) and (distancia2 > distancia3):
    print(f"maior distancia: {distancia2}")
else:
    print(f"maior distancia: {distancia3}")

