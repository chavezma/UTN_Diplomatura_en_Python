import os

"""
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""

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
            print(
                f"producto elegido [{compra[idx][0]}] [{compra[idx][1]}] [{compra[idx][2]}]" # noqa
            )
            encargo = input(
                "Ingrese los nuevos valores cantidad-precio (separados por guion): " # noqa
            )
            cantidad, precio = encargo.split("-")
            compra[idx] = (prod, cantidad, precio)

            print(f"se modificó el {prod} de la posicion {idx}.")
            print(
                f"producto modificado [{compra[idx][0]}] [{compra[idx][1]}] [{compra[idx][2]}]" # noqa
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
    for articulo in compra:
        if articulo[0] == "":
            continue
        total_articulo = int(articulo[1]) * int(articulo[2])
        print(
            f"{articulo[0].ljust(15)} {articulo[1]} x {articulo[2]} = {total_articulo}"  # noqa
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
