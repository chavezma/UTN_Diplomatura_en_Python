"""
A partir del ejercicio 5 cree un programa que vaya
agregando en una lista las compras realizadas.
"""

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
