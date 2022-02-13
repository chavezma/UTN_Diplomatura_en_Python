import math

"""
Escriba un programa que solicite el radio de una
circunferencia y permita calcular el área.
Presente el resultado en la terminal del editor.
"""

radio = int(input("Ingrese el radio: "))
area = math.pi * (radio**2)
print(f"El área es {area}")
