from view import Application
from model import ProductFactory


class Controller:
    """Clase Controller que funciona como Controlador del patron MVC, que instancia y coordina
    las instancias del Modelo y la Vista
    """

    def __init__(
        self,
    ):
        self.manager = ProductFactory()
        self.view = Application(self)

    def get_producto_por_index(self, index):
        """Pide al modelo un Producto

        :param index: Indice del producto en la grilla que corresponde con el listado interno del modelo
        :type index: int
        :return: instancia del producto
        :rtype: Producto
        """
        return self.manager.productos[index]

    def get_productos(
        self,
    ):
        """Pide al modelo el listado de productos existentes

        :return: Lista de objetos productos cargados
        :rtype: list(Producto)
        """
        return self.manager.get_productos()

    def get_productos_por_nombre(
        self,
        nombre,
        criterio,
    ):
        """Pide al modelo el listado de productos que cumplan con el criterio indicado sobre el campo nombre

        :return: Lista de objetos productos encontrados
        :rtype: list(Producto)
        """
        return self.manager.buscar(nombre, criterio)

    def alta(self, nombre, cantidad, precio):
        """Pide al modelo generar un nuevo producto con los parametros indicados

        :param nombre: Nombre del producto que cargó el usuario
        :type nombre: str
        :param cantidad: Cantidad de producto a agregar
        :type cantidad: int
        :param precio: Precio unitario del producto a agregar
        :type precio: float
        :return: objeto producto generado.
        :rtype: Producto
        """
        return self.manager.crear_producto(nombre, cantidad, precio)

    def borrar(self, index):
        """Pide al modelo que elimine el producto indexado por el valor de ´index´

        :return: id del objeto producto eliminado
        :rtype: int
        """
        return self.manager.borrar_producto(index)

    def actualizar_producto(self, index, prod):
        """Pide al modelo que actualice el producto indexado por el valor de ´index´ con los valores de ´prod´

        :param index: Indice del producto afectado para la actualización
        :type index: int
        :param prod: objeto producto con los nuevos valores a actualizar
        :type prod: Producto
        :return: id del objeto producto eliminado
        :rtype: int
        """
        return self.manager.modificar_producto(index, prod)


if __name__ == "__main__":
    mi_app = Controller()
