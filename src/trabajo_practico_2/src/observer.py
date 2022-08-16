
class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, prod):
        print(f"El observer {self.name} ha afectado al producto {prod}")
