import sys

"""
(Este es el ejercicio 2 de la unidad 1 pero implementando if/else
Cree un programa que incorpore el módulo sys, al cual desde la terminal
se le puedan pasar tres parámetros. El programa debe tomar los parámetros
e indicar en la terminal si son múltiplos de dos. Utilice la estructura if/else
"""
if len(sys.argv) != 4:
    print("Este programa espera 3 parametros.")

v1 = int(sys.argv[1])
v2 = int(sys.argv[2])
v3 = int(sys.argv[3])

if (v1 % 2) == 0:
    print(f"v1 = {v1} es multiplo de 2.")
else:
    print(f"v1 = {v1} no es multiplo de 2.")

if (v2 % 2) == 0:
    print(f"v2 = {v2} es multiplo de 2.")
else:
    print(f"v2 = {v2} no es multiplo de 2.")

if (v3 % 2) == 0:
    print(f"v3 = {v3} es multiplo de 2.")
else:
    print(f"v3 = {v3} no es multiplo de 2.")
