import sys

"""
Tome el ejercicio de cálculo de números pares e impares
de la unidad 2 y agréguele un bucle al código de forma de simplificarlo.
"""

for idx in range(1, len(sys.argv)):
    numero = int(sys.argv[idx])
    if (numero % 2) == 0:
        print(f"v = {numero} es multiplo de 2.")
    else:
        print(f"v = {numero} no es multiplo de 2.")
