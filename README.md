# UTN_Diplomatura_en_Python

## Introducción

En este repositorio, pretendo ir realizando la ejercitación y trabajos prácticos del curso de Python en la UTN y a su vez, ir practicando la ulitización de esta herramienta de versionado.

## Ejercitacion

## Unidad 1

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

## Unidad 2

#### Ejercicio 1:

(Este es el ejercicio 2 de la unidad 1 pero implementando if/else. Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si son múltiplos de dos. Utilice la estructura if/else

```python
import sys

if len(sys.argv) != 4:
    print("Este programa espera 3 parametros.")

v1 = int(sys.argv[1])
v2 = int(sys.argv[2])
v3 = int(sys.argv[3])

if v1 % 2 == 0:
    print(f"v1 = {v1} es multiplo de 2.")
else:
    print(f"v1 = {v1} no es multiplo de 2.")

if v2 % 2 == 0:
    print(f"v2 = {v2} es multiplo de 2.")
else:
    print(f"v2 = {v2} no es multiplo de 2.")

if v3 % 2 == 0:
    print(f"v3 = {v3} es multiplo de 2.")
else:
    print(f"v3 = {v3} no es multiplo de 2.")
```

#### Ejercicio 2:

Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración conteniendo los dos elementos de la lista concatenándolos con texto para formar una oración con sentido. Presente el resultado en la terminal del editor.

```python
canasta_frutas = ["manzana", "naranja"]

print(f"En la canasta de frutas tenemos {canasta_frutas[0]}s")
print(f"y tambien tenemos {canasta_frutas[1]}s.")
```

#### Ejercicio 3:

Tome dos valores por consola, y guarde en una lista: [primer_valor, segundo_valor, la_suma_de_los_valores]
Presente el resultado en la terminal del editor.

```python
valores = []

valores.append(int(input("Ingrese el primer valor:")))
valores.append(int(input("Ingrese el segundo valor:")))
valores.append(int(valores[0])+int(valores[1]))

print(f"usted ingreso: {valores}")
```

#### Ejercicio 4:

Realice un programa que consulte la edad y en caso de que el valor ingresado supere la fecha de jubilación, presente en la terminal el mensaje "Ya esta en edad de jubilarse" en caso contrario que presente “Aún está en edad de trabajar".

```python
EDAD_JUBILATORIO = 65

edad = int(input("Ingrese su edad:"))

if edad >= EDAD_JUBILATORIO:
    print("Ya esta en edad de jubilarse")
else:
    print("Aún está en edad de trabajar")

```

#### Ejercicio 5:

Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una función, de forma que la operacion se realice dentro de la misma Presente el resultado en la terminal del editor.

```python
import math

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
```
