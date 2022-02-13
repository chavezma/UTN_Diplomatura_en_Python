import sys

"""
Cree un programa que incorpore el módulo sys, al cual desde la terminal
se le puedan pasar tres parámetros. El programa debe tomar los parámetros
e indicar en la terminal si son múltiplos de dos.
"""

if len(sys.argv) != 4:
    print("Este programa espera 3 parametros.")

v1 = int(sys.argv[1])
v2 = int(sys.argv[2])
v3 = int(sys.argv[3])

if v1 % 2 == 0 and v2 % 2 == 0 and v3 % 2 == 0:
    print("Todos los parametros son multiplis de dos.")
else:
    print("Alguno de los parametros no es multiplo de dos.")
