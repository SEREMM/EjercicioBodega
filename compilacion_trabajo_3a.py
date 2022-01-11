
hrs = input("ingrese horas laboradas: ")
tarifa = input("ingrese tarifa designada por hora: ")
hrsext = 0
tarifaext = 0
totalextra = 0
hrs = float(hrs)
tarifa = float(tarifa)

if hrs > 40:
    hrsext = hrs - 40
    tarifaext = tarifa * 1.5
    hrsext = hrsext * tarifaext
    totalextra = hrsext + (40 * tarifa)
    print("total acumulado más horas extra: ", totalextra)

else:
    total = hrs * tarifa
    print("total acumulado: " ,total)
