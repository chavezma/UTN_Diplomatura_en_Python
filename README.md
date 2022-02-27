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

## Unidad 2

#### Ejercicio 01:

Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo.

```python
    for idx in range(1, len(sys.argv)):
        numero = int(sys.argv[idx])
        if (numero % 2) == 0:
            print(f"v = {numero} es multiplo de 2.")
        else:
            print(f"v = {numero} no es multiplo de 2.")
```

#### Ejercicio 02:

Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”.

```python
    oracion = input("Ingrese una oración:")
    contador = 0

    for char in oracion:
        if char == 'a' or char == 'A':
            contador += 1

    print(f"La oracion contiene {contador} letras 'a'")
```

#### Ejercicio 03:

Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparecen todas las bocales considerando minúsculas, mayúsculas y acentos.

```python
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
```

#### Ejercicio 04:

Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido.

```python
    edad = int(input("Ingrese su edad:"))

    print("Usted ha cumplido los siguientes años:")
    for anio in range(1, edad + 1):
        print(anio)
```

#### Ejercicio 05:

Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado.

```python
    total = 0

    while True:
        encargo = input("Ingrese producto-cantidad-precio (separados por guion): ")
        producto, cantidad, precio = encargo.split('-')
        total += int(cantidad) * int(precio)

        while True:
            mas = input("Lleva algo mas [Si/No]?")
            if mas == "Si" or mas == "No":
                break

        if mas == "No":
            print(f"El total de la compra es de ${total} pesos")
            break
```

#### Ejercicio 06:

A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas.

```python
    compra = list()
    total_articulo = 0
    total_compra = 0

    while True:
        encargo = input("Ingrese producto-cantidad-precio (separados por guion): ")
        producto, cantidad, precio = encargo.split("-")
        compra.append((producto, cantidad, precio))

        while True:
            mas = input("Lleva algo mas [Si/No]?")
            if mas == "Si" or mas == "No":
                break

        if mas == "No":
            for articulo in compra:
                total_articulo = int(articulo[1]) * int(articulo[2])
                total_compra += total_articulo
                print(
                    f"{articulo[0].ljust(15)} {articulo[1]} x \
                        {articulo[2]} = {total_articulo}"
                )

            print(f"Total Compra             {total_compra}")
            print("")
            break

```

#### Ejercicio 07:

A partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas.

```python
    def calcular_compra(productos: dict):
        importe = 0
        print("--------------------------------------------------------")
        print("FACTURA")
        print("--------------------------------------------------------")
        for elemento in productos.items():
            cantidad, valor = elemento[1]
            total = int(cantidad) * int(valor)
            print(f"{elemento[0].ljust(15)}      {cantidad} x {valor} = {total}")
            importe += total
        print(f"Total Compra                 {importe}")
        print("")


    compra = {}

    while True:
        encargo = input("Ingrese producto-cantidad-precio (separados por guion): ")
        producto, cantidad, precio = encargo.split("-")

        compra[producto] = (cantidad, precio)

        while True:
            mas = input("Lleva algo mas [Si/No]?")
            if mas == "Si" or mas == "No":
                break

        if mas == "No":
            calcular_compra(compra)
            break

```

#### Ejercicio 08:

A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

```python
    compra = list()
    menu = dict()

    menu["1"] = "alta"
    menu["2"] = "baja"
    menu["3"] = "consulta"
    menu["4"] = "modificar"
    menu["5"] = "salir"


    def salir():
        print("")
        print("Gracias por usar nuestro sistema.")
        input("Presione cualquier tecla para finalizar...")
        print("")


    def clearConsole():
        command = "clear"
        if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
            command = "cls"
        os.system(command)


    def buscar(elem, lista):
        for idx in range(0, len(lista)):
            if lista[idx][0] == elem:
                return idx
        return -1


    def listar_menu():
        clearConsole()
        for key, value in menu.items():
            print(f"[{key}] - {value}")

        opt = input("Ingrese el nro de opcion que desea realizar:")

        if opt in menu:
            return menu[opt]

        return "none"


    def continuar():
        while True:
            mas = input("Desea repetir la operacion [S/N]?")
            if mas.upper() == "S" or mas.upper() == "N":
                break

        if mas == "N":
            return False
        else:
            return True


    def alta():
        resp = True
        while resp:
            encargo = input("Ingrese producto-cantidad-precio (separados por guion): ") # noqa
            producto, cantidad, precio = encargo.split("-")
            compra.append((producto, cantidad, precio))

            resp = continuar()


    def baja():
        resp = True
        idx = -1
        while resp:
            prod = input("Ingrese el producto que desea quitar: ")
            idx = buscar(prod, compra)
            if idx != -1:
                del compra[idx]
                print(f"se quito el {prod} de la posicion {idx}.")
            else:
                print(f"El producto {prod} no existe.")

            resp = continuar()


    def modificar():
        resp = True
        idx = -1
        while resp:
            prod = input("Ingrese el producto que desea modificar: ")
            idx = buscar(prod, compra)
            if idx != -1:
                print(f"producto elegido [{compra[idx][0]}] [{compra[idx][1]}] [{compra[idx][2]}]") # noqa
                encargo = input("Ingrese los nuevos valores producto-cantidad-precio (separados por guion): ") # noqa
                producto, cantidad, precio = encargo.split("-")
                compra[idx] = (producto, cantidad, precio)

                print(f"se modificó el {prod} de la posicion {idx}.")
                print(f"producto modificado [{compra[idx][0]}] [{compra[idx][1]}] [{compra[idx][2]}]") # noqa
            else:
                print(f"El producto {prod} no existe.")

            resp = continuar()

        print("")
        input("presione cualquier tecla para volver al menu...")


    def consulta():
        clearConsole()
        print("--------------------------------------------------------")
        print("FACTURA")
        print("--------------------------------------------------------")
        for articulo in compra:
            if articulo[0] == '':
                continue
            total_articulo = int(articulo[1]) * int(articulo[2])
            print(
                f"{articulo[0].ljust(15)} {articulo[1]} x {articulo[2]} = {total_articulo}" # noqa
            )
        print("")
        input("presione cualquier tecla para volver al menu...")
        clearConsole()


    while True:
        selected = ""
        while selected != "salir":
            selected = listar_menu()

            if selected == "none":
                continue

            result = eval(selected + "()")
            # selected = ""
        break

```

#### Ejercicio 09:

A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
Pregunta: Considera que es más fácil guardar la información en listas o en diccionarios

```python

```

#### Ejercicio 10:

Escriba un programa que guarde en una variable una contraseña y consulte al usuario por la contraseña hasta que esta sea correcta.
El programa debe informar al usuario si la contraseña fue correcta o no.

```python
    contrasenia = "Learning"
    intentos = 5


    while intentos > 0:
        adivina = input("Intente adivinar la contraseña, ingrese una: ")
        if contrasenia == adivina:
            print("Has adivinado!!!")
            break

        intentos -= 1
        print(f"No adivinaste, te quedan {intentos} intentos.")
```
