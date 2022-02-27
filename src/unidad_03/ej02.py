"""
Escriba un programa que consulte al usuario por
una oración y comente al usuario cuantas veces aparece la letra “a”.
"""

oracion = input("Ingrese una oración:")
contador = 0

for char in oracion:
    if char == 'a' or char == 'A':
        contador += 1

print(f"La oracion contiene {contador} letras 'a'")
