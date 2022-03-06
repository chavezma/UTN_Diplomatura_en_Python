"""
Crear una función lambda que tome como parámetro una frase y la escriba al revés.
"""

reverse = lambda frase: ''.join(frase[i] for i in range(len(frase) - 1, -1, -1))
print(reverse("mi oracion es una fiesta"))
