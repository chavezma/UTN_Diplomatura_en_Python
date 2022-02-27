"""
Escriba un programa que consulte al usuario por una oración
y comente al usuario cuantas veces aparecen todas las bocales
considerando minúsculas, mayúsculas y acentos.
"""

oracion = input("Ingrese una oración:")
contador = 0
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'A',
           'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']
contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for index in range(0, len(vocales)):
    cant = oracion.count(vocales[index])
    contadores[index] = cant

for index in range(0, len(vocales)):
    print(f"[{vocales[index]}] = {contadores[index]}")
