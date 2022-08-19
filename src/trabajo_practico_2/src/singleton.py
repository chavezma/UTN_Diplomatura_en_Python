class Singleton:
    """Clase que se utilizara como decorador para instaciar la base como Singleton. Para permitir unicamente una sola conexion a la base a la vez.
    """
    def __init__(self, cls):
        self._cls = cls

    def instance(self):
        """Función que controla que el objeto no se haya instanciado previamente. Si no existe, si retorna una nueva instancia.

        :return: instancia nueva o existente.
        :rtype: :class: ´Singleton´
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        """Función que controla que no se intente instanciar mediante el uso de paréntesis."""

        raise TypeError("Se debe acceder mediante el método `Instance()`.")
