import math

"""
Escriba un programa que solicite el perímetro.
Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
L = 2 · pi · r
"""

radio = int(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
print(f"El perimetro es {perimetro}")
