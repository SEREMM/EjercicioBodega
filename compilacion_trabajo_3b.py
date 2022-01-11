
score = input("Ingresa puntaje (selecciona valores entre 0.0[mínimo] y 1.0[máximo]): ")
score1 = 0

try:
    score1 = float(score)
except:
    score1 = -1

if score1 > 1.0 :
    print("ERROR, ingrese valor entre 0.0 a 1.0")
elif score1 == 1.0 :
    print("A")
elif score1 >= 0.9 :
    print("A")
elif score1 >= 0.8 :
    print("B")
elif score1 >= 0.7 :
    print("C")
elif score1 >= 0.6 :
    print("D")
elif score1 > 0.0 :
    print("F")
else :
    print("ERROR, ingrese valor entre 0.0 a 1.0")
