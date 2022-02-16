"""
Tome dos valores por consola, y guarde en una lista:
[primer_valor, segundo_valor, la_suma_de_los_valores]
Presente el resultado en la terminal del editor.
"""

valores = []

valores.append(int(input("Ingrese el primer valor:")))
valores.append(int(input("Ingrese el segundo valor:")))
valores.append(int(valores[0])+int(valores[1]))

print(f"usted ingreso: {valores}")
