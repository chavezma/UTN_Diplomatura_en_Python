from database import Database
import re


class Producto:
    """Clase que representa un producto del modelo de datos

    :param nombre: Nombre que identifica el producto
    :type nombre: str
    :param cantidad: Cantidad a agregar de ese producto
    :type cantidad: int
    :param precio: Precio del producto a agregar
    :type precio: float
    :param id: Id del producto en la base de datos, por defecto None
    :type id: int, optional
    """

    def __init__(
        self,
        nombre,
        cantidad,
        precio,
        id=None,
    ):
        """Metodo Constructor"""
        patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena

        if nombre is None or nombre == "":
            raise Exception("Error: Debe ingresar un nombre para el producto")

        if not re.match(patron, nombre):
            raise Exception(
                "Error: El nombre del producto es inválido. \nSolo puedo contener letras."
            )
        try:
            cantidad = int(cantidad)
        except Exception as e:
            raise Exception("Error: La cantidad debe ser un número entero válido")

        if cantidad < 1:
            raise Exception("Error: La cantidad debe ser un número positivo")

        try:
            precio = float(precio)
        except Exception as e:
            raise Exception("Error: La cantidad debe ser un número valido")

        if precio <= 0:
            raise Exception("Error: El precio debe ser un número mayor que cero")

        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.__db = Database.instance()

    def alta(
        self,
    ):
        """Método que resuelve el alta del producto en la base de datos."""
        self.id = self.__db.insert(self)

    def borrar(
        self,
    ):
        """Método que resuelve la eliminación del producto en la base de datos."""
        self.__db.delete(self)

    def actualizar(
        self,
    ):
        """Método que resuelve la actualización del producto en la base de datos."""
        self.__db.update(self)

    def __str__(
        self,
    ):
        """Método que implementa una sobrecarga del metodo especial ´__str__´."""
        return (
            "{ id: "
            + str(self.id)
            + ", nombre: "
            + str(self.nombre)
            + ", cantidad: "
            + str(self.cantidad)
            + ", precio: "
            + str(self.precio)
            + "}"
        )

    def __repr__(
        self,
    ):
        """Método que implementa una sobrecarga del metodo especial ´__repr__´."""
        return (
            "{ id: "
            + str(self.id)
            + ", nombre: "
            + str(self.nombre)
            + ", cantidad: "
            + str(self.cantidad)
            + ", precio: "
            + str(self.precio)
            + "}"
        )


class ProductFactory:
    """Clase que gestiona los diferentes productos que se cargan en la vista."""

    def __init__(
        self,
    ):
        self.productos = []
        self.__db = Database.instance()

    def crear_producto(
        self,
        nombre,
        cantidad,
        precio,
    ):
        """Toma los valores que ingresaron por la vista e invoca
            el metodo propio del producto para su alta.

        :param nombre: Nombre del producto que cargó el usuario
        :type nombre: str
        :param cantidad: Cantidad de producto a agregar
        :type cantidad: int
        :param precio: Precio unitario del producto a agregar
        :type precio: float
        :return: id de producto que se acaba de generar
        :rtype: int
        """
        prod = Producto(nombre, cantidad, precio)
        prod.alta()
        self.productos.append(prod)
        return prod.id

    def get_productos(
        self,
    ):
        """Busca en la base de datos los productos cargados y los envia a la vista.

        :return: Lista de objetos :class: ´Producto´
        :rtype: list
        """
        self.productos = []
        lista_prod = self.__db.get_many_products()

        for prod in lista_prod:
            unprod = Producto(prod[1], prod[2], prod[3], prod[0])
            self.productos.append(unprod)

        return lista_prod

    def borrar_producto(self, index):
        """Toma el objeto Producto en la lista de productos, invoca su metodo de borrado y actualiza la lista interna.

        :param index: Indice del producto a borrar en el listado interno.
        :type index: int
        :return: id de producto que se acaba de borrar
        :rtype: int
        """
        id = self.productos[index].id
        self.productos[index].borrar()
        self.productos = self.productos[0:index] + self.productos[index + 1:]
        return id

    def modificar_producto(self, index, prod):
        """Toma el objeto Producto en la lista de productos, invoca su metodo de borrado y actualiza la lista interna.

        :param index: Indice del producto en el listado interno que se debe actualizar.
        :type index: int
        :param prod: Objeto de :class: ´Producto´ con los valores a actualizar.
        :type prod: int
        :return: id de producto que se acaba de actualizar
        :rtype: int
        """
        prod.actualizar()
        self.productos[index] = prod

        return id

    def buscar(self, nombre, condicion):
        """Dado un nombre y una condicion, realiza la busqueda en la base de datos.

        :param nombre: Nombre o parte del nombre del producto que se desea buscar.
        :type nombre: str
        :param condicion: Valores que indican el tipo de filtro a usar ´Comienza con´, ´Termina con´ o ´Contiene´
        :type condicion: str
        :return: lista de :class: ´Producto´ con el resultado de la busqueda
        :rtype: list
        """
        if nombre is None or nombre == "":
            raise Exception(
                "Error: Para buscar un producto es necesario indicar algun valor de nombre"
            )

        if condicion is None or condicion == "":
            raise Exception(
                "Error: Para buscar un producto es necesario indicar una condición"
            )

        self.productos = []
        lista_prod = self.__db.find_products(nombre, condicion)

        for prod in lista_prod:
            unprod = Producto(prod[1], prod[2], prod[3], prod[0])
            self.productos.append(unprod)

        return lista_prod
