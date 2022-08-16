
class Observer:
    """Clase que representa al objeto que observa.
    :param name: Nombre descriptivo del observador
    :type name: str
    """
    def __init__(self, name):
        self.name = name

    def update(self, prod):
        """Funcion que realiza la acción correspondiente al recibir aviso de la actualizacion del observable.
        :param prod: Objeto producto que fue afectado
        :type prod: Producto
        """
        print(f"El observer {self.name} ha recibido notifiacion de cambios sobre el producto {prod}")
