#EJERCICIOS PRÁCTICAS
"""ME QUEDÉ EN LA PARTE 5"""
n = input("introduzca su nombre: ")

print("bienvenido ", n)

a = input("ingrese un número al azar: ")
b = input("ingrese un segundo número al azar: ")

try:
    a = float(a)
    b = float(b)
except ValueError:
    print("ingrese solo valores numericos")

print("resultado de suma:", a + b)
print("resultado de resta:", a - b)
print("resultado de multiplicación:", a * b)
print("resultado de división:", a / b)
print("resultado al cuadrado:", a ** b)
print("resultado de resto:", a % b)

if a > b:
    print("primer número ingresado es mayor")
elif a < b:
    print("segundo número ingresado es mayor")
else:
    print("los números son iguales")
