# UTN_Diplomatura_en_Python

## Introducción

En este repositorio, pretendo ir realizando la ejercitación y trabajos prácticos del curso de Python en la UTN y a su vez, ir practicando la ulitización de esta herramienta de versionado.

## Ejercitacion

### Unidad 1

#### Ejercicio 1:

Cree un programa que tome tres valores por consola multiplique el primero por el segundo
y le sume el tercero. Presente el resultado en la terminal

```python
v1 = int(input("ingrese primer valor:"))
v2 = int(input("ingrese segundo valor:"))
v3 = int(input("ingrese tercer valor:"))

res = (v1 * v2) + v3

print(f"el resultado es: {res}")
```

#### Ejercicio 2:

Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos.

```python
if len(sys.argv) != 4:
    print("Este programa espera 3 parametros.")

v1 = int(sys.argv[1])
v2 = int(sys.argv[2])
v3 = int(sys.argv[3])

if v1 % 2 == 0 and v2 % 2 == 0 and v3 % 2 == 0:
    print("Todos los parametros son multiplis de dos.")
else:
    print("Alguno de los parametros no es multiplo de dos.")
```

#### Ejercicio 3:

Escriba un programa que solicite el perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:

- L = 2 · $\pi$ · r
- L = Longitud de perímetro
- $\pi$ = Número pí igual a 3.1416
- r = Radio

```python
import math

radio = int(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
print(f"El perimetro es {perimetro}")
```

#### Ejercicio 4:

Escriba un programa que solicite el radio de una circunferencia y permita calcular el
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:

- A = $\pi$ · $r^2$
- A = Área
- $\pi$ = Número pi igual a 3.1416
- r = Radio

```python
import math

radio = int(input("Ingrese el radio: "))
area = math.pi * (radio**2)
print(f"El área es {area}")
```

#### Ejercicio 5:

Escriba un programa que solicite un valor entero por pantalla y presente en la terminal editor el valor incrementado en un 10%.

```python
valor = int(input("ingrese un numero positivo: "))
incrementa = valor * 1.1
print(f"El valor incrementado en un 10% es igual a {incrementa}")
```
