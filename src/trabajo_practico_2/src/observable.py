import enum

class DBEvents(enum.Enum):
    Insert = 1
    Update = 2
    Delete = 3

class DBObservable:

    def __init__(self, events: DBEvents):
        self.observers = {event: dict() for event in events}

    def get(self, event: DBEvents):
        return self.observers[event]

    def add(self, o, event: DBEvents, callback=None):
        if callback is None:
            callback = getattr(o, 'update')

        self.get(event)[o] = callback

    def remove(self, o, event: DBEvents):
        del self.get(event)[o]

    def notify(self, event: DBEvents, prod):
        for o, call in self.get(event).items():
            call(prod)
