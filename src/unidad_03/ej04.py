"""
Escriba un programa que solicite la edad de la persona
e imprima todos los años que la persona ha cumplido.
"""

edad = int(input("Ingrese su edad:"))

print("Usted ha cumplido los siguientes años:")
for anio in range(1, edad + 1):
    print(anio)
