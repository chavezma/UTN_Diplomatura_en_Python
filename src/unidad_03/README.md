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
        if os.name in ("nt", "dos"):
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
