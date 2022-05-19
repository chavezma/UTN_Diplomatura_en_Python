from view import View
from model import Model
import re

class Controller:

    def __init__(self,):
        self.model = Model()
        self.view = View(self)

    def getProductos(self):
        return self.model.getProductos()

    def alta(self, nombre, cantidad, precio):
        return self.model.alta(nombre, cantidad, precio)

    def borrar(self, id):
        return self.model.borrar(id)

    def actualizar(self, id, nombre, cantidad, precio):
        return self.model.actualizar(id, nombre, cantidad, precio)

    def main(self):
        self.view.mainloop()


if __name__ == "__main__":
    mi_app = Controller()
    mi_app.main()
