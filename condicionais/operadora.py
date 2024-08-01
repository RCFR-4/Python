quant_min = int(input("digite a quantidade de minutos: "))

if quant_min <= 100:
    print("valor total a pagar: R$ 50.00")
else:
    sobra = quant_min % 100
    total_pagar = (sobra * 2) + 50

    print(f"valor total a pagar: {total_pagar:.2f}")
