"""
Suponga que tiene una verdulería y carga la cantidad y el
precio de lo comprado por un cliente. Realice un programa
que tome de a uno la cantidad y el precio comprado por el
cliente y al finalizar la compra retorne el monto total gastado.
"""

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
