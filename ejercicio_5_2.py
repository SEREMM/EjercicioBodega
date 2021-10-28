#variables lar:largest, sma:smallest, val:valor, fval:valor float
lar = -1
sma = -1

#bucle
while True:
#while i!=4:
    val = input("Ingrese varios números, cuando termine, ingrese 'hecho': ")
    try:
        fval = float(val)
    except:
        if val == "hecho" : break
        print("Valor inválido")

    if fval > lar:
        lar = fval
    if sma == -1:
        sma = fval
    elif fval < sma:
        sma = fval
    #i = i + 1
print("Máximo es", lar)
print("Mínimo es", sma)
