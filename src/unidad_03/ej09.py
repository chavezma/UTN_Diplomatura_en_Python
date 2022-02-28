"""
A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
Pregunta: Considera que es más fácil guardar la información en
listas o en diccionarios
"""

import os

"""
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""

compra = dict()
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
    clearConsole()


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
        encargo = input(
            "Ingrese producto-cantidad-precio (separados por guion): "
        )  # noqa
        producto, cantidad, precio = encargo.split("-")
        compra[producto] = {"cantidad": cantidad, "precio": precio}

        resp = continuar()


def baja():
    clearConsole()
    print(f"elementos en factura {compra.keys()}")
    resp = True
    while resp:
        prod = input("Ingrese el producto que desea quitar: ")
        if prod in compra:
            del compra[prod]
            print(f"se quito el {prod} de la lista de compra.")
        else:
            print(f"El producto {prod} no existe.")

        resp = continuar()


def modificar():
    resp = True
    clearConsole()
    print(f"elementos en factura {compra.keys()}")
    while resp:
        prod = input("Ingrese el producto que desea modificar: ")
        if prod in compra:
            print(
                f"producto elegido [{prod}] [{compra[prod]['cantidad']}] [{compra[prod]['precio']}]"  # noqa
            )
            encargo = input(
                "Ingrese los nuevos valores cantidad-precio (separados por guion): "  # noqa
            )
            cantidad, precio = encargo.split("-")
            compra[prod] = {"cantidad": cantidad, "precio": precio}

            print(f"se modificó el {prod} de la lista de compra.")
            print(
                f"producto modificado [{prod}] [{compra[prod]['cantidad']}] [{compra[prod]['precio']}]"  # noqa
            )
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
    for item, values in compra.items():
        total_articulo = int(values["cantidad"]) * int(values["precio"])
        print(
            f"{item.ljust(15)} {values['cantidad']} x {values['precio']} = {total_articulo}"  # noqa
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
    break
