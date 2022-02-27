"""
A partir del ejercicio 5 cree un programa que vaya
agregando en un diccionario las compras realizadas.
"""


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
