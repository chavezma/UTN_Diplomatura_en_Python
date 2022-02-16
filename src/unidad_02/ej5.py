import math

"""
Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando
de utilizar una función, de forma que la operacion se realice dentro de
la misma Presente el resultado en la terminal del editor.
"""

PORC_INCRE = 10  # Incremento del 10%


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


def calcular_area_circulo(radio):
    return math.pi * (radio**2)


def calcular_incremento(valor, porcentaje_incremento):
    return valor * (1 + (porcentaje_incremento / 100))


radio = int(input("ingrese el valor de radio: "))
valor = int(input("ingrese un numero positivo: "))

print(f"El perimetro es {calcular_perimetro_circulo(radio)}")
print(f"El área es {calcular_area_circulo(radio)}")
print(f"El valor incrementado es {calcular_incremento(valor, PORC_INCRE)}")
