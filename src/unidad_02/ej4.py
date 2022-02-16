"""
Realice un programa que consulte la edad y en caso de
que el valor ingresado supere la fecha de jubilación,
presente en la terminal el mensaje "Ya esta en edad de jubilarse" en
caso contrario que presente “Aún está en edad de trabajar".
"""

EDAD_JUBILATORIO = 65

edad = int(input("Ingrese su edad:"))

if edad >= EDAD_JUBILATORIO:
    print("Ya esta en edad de jubilarse")
else:
    print("Aún está en edad de trabajar")
