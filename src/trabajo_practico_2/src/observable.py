import enum

class DBEvents(enum.Enum):
    """Clase que enumera los distintos tipos de eventos que se observaran."""
    Insert = 1
    Update = 2
    Delete = 3

class DBObservable:
    """Clase que representa al objeto que sera observado.
    :param events: Listado de eventos posibles que se observaran
    :type events: DBEvents
    """
    def __init__(self, events: DBEvents):
        self.observers = {event: dict() for event in events}

    def get(self, event: DBEvents):
        """Función para devolver los observadores de un determinado evento.

        :param event: Evento que se desea obtener
        :type event: DBEvents
        :return: observadores del evento
        :rtype: Observer
        """

        return self.observers[event]

    def add(self, observer, event: DBEvents, callback=None):
        """Función para subscribir observadores.

        :param observer: Evento que se desea obtener
        :type observer: Observer
        :param event: Evento que se desea obtener
        :type event: DBEvents
        :param callback: Funcion de notificación custom
        :type callback: Function
        """
        if callback is None:
            callback = getattr(observer, 'update')

        self.get(event)[observer] = callback

    def remove(self, observer, event: DBEvents):
        """Función para desubscribir observadores.

        :param observer: Objeto observador a remover
        :type observer: Observer
        :param event: Evento del observador que se desea remover
        :type event: DBEvents
        """
        del self.get(event)[observer]

    def notify(self, event: DBEvents, prod):
        """Función para notificar a los observadores de un determinado evento.

        :param event: Evento que se desea notificar
        :type event: DBEvents
        :param prod: Objeto producto para el cual se disparo el evento
        :type prod: Producto
        """
        for o, call in self.get(event).items():
            call(prod)
