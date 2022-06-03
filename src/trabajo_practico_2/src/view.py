import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from model import Producto


class Application:
    """Clase que representa a la aplicación principal.

    :param controller: Controlador que vinculará la vista con el modelo.
    :type controller: Controller
    """

    def __init__(
        self,
        controller,
    ):
        self.app = QtWidgets.QApplication(sys.argv)
        self.the_view = MainWindow(controller)
        self.the_view.setFixedHeight(398)
        self.the_view.setFixedWidth(491)
        self.the_view.show()
        sys.exit(self.app.exec_())


class BuscarProdWindow(QDialog):
    """Clase que representa a una ventana secundaria (Modal) para mostrar la busqueda de un producto.

    :param parent: Aplicación/Ventana padre
    :type parent: MainWindow
    :param controller: Controlador para acceder al modelo.
    :type controller: Controller
    """

    def __init__(
        self,
        parent,
        controller,
    ):
        self.controller = controller
        self.parent = parent
        super().__init__(self.parent)
        loadUi(
            os.path.join(os.path.abspath(__file__), "../view", "buscarProd.ui"), self
        )

        self.cmb_buscar.addItems(["Empieza con", "Termina con", "Contiene"])
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def launch(
        self,
    ):
        """Función para invocar la pantalla de busqueda, dejando la ventana principal en segundo plano."""
        ret = self.exec_()
        if ret == 1:
            return self.lst_prod

    def cancelar(
        self,
    ):
        """Función asociada al click del boton Cancelar para volver a la ventana principal sin realizar ninguna acción."""
        self.close()

    def buscar(
        self,
    ):
        """Función asociada al click del boton Buscar para efecutar la busqueda de un producto."""
        nombre = self.ipt_nombre.text()
        criterio = self.cmb_buscar.currentText()

        if nombre == "":
            continuar = QMessageBox.critical(
                self,
                "Buscar Producto",
                "Para buscar un producto debe ingresar algun valor de nombre",
                QMessageBox.Ok,
            )
            return

        try:
            message = ""
            self.lst_prod = self.controller.get_productos_por_nombre(nombre, criterio)

            if len(self.lst_prod) == 0:
                continuar = QMessageBox.information(
                    self,
                    "Buscar Producto",
                    "No se han encontrado productos con el criterio elegido.",
                    QMessageBox.Ok,
                )
                return

        except Exception as e:
            message = "BuscarProd: Ocurrió un error al intentar buscar \n"
            message += f"error crear producto message: [{e}]"
            continuar = QMessageBox.critical(
                self, "Buscar Producto", message, QMessageBox.Ok
            )
        else:
            self.accept()


class ModProdWindow(QDialog):
    """Clase que representa a una ventana secundaria (Modal) para mostrar la modificación de un producto.

    :param prod: objeto producto con la información del producto a modificar.
    :type prod: Producto
    :param parent: Aplicación/Ventana padre
    :type parent: MainWindow
    """

    def __init__(
        self,
        prod,
        parent,
    ):
        self.prod = prod
        self.parent = parent
        super().__init__(self.parent)
        loadUi(
            os.path.join(os.path.abspath(__file__), "../view", "modificarProducto.ui"),
            self,
        )

        self.ipt_precio.setValidator(QDoubleValidator())
        self.ipt_cantidad.setValidator(QIntValidator())

        self.ipt_nombre.setText(str(self.prod.nombre))
        self.ipt_cantidad.setText(str(self.prod.cantidad))
        self.ipt_precio.setText(str(self.prod.precio))

        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def launch(
        self,
    ):
        """Función para invocar la pantalla de modificación, dejando la ventana principal en segundo plano."""
        ret = self.exec_()
        if ret == 1:
            return self.prod

    def cancelar(
        self,
    ):
        """Función asociada al click del boton Cancelar para volver a la ventana principal sin realizar ninguna acción."""
        self.close()

    def guardar(
        self,
    ):
        """Función asociada al click del boton Guardar para efecutar la persistencia del producto en el modelo."""
        nombre = self.ipt_nombre.text()
        cantidad = self.ipt_cantidad.text()
        precio = self.ipt_precio.text()

        continuar = QMessageBox.question(
            self,
            "Modificar Producto",
            "¿Esta seguro que desea modificar el producto?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if continuar == QMessageBox.No:
            return

        id = self.prod.id
        try:
            message = ""
            self.prod = Producto(nombre, cantidad, precio, id)
        except Exception as e:
            message = "ModifProd: Ocurrió un error al intentar actualizar \n"
            message += f"error crear producto message: [{e}]"
            continuar = QMessageBox.critical(
                self, "Modificar Producto", message, QMessageBox.Ok
            )
        else:
            self.accept()


class MainWindow(QMainWindow):
    """Clase que representa la ventana principal de la aplicación de gestión de productos.

    :param controller: objeto que vincula la vista con el modelo.
    :type controller: Controller
    """

    def __init__(
        self,
        controller,
    ):
        super(
            MainWindow,
            self,
        ).__init__()
        self.controller = controller
        loadUi(os.path.join(os.path.abspath(__file__), "../view", "main.ui"), self)

        self.ipt_precio.setValidator(QDoubleValidator())
        self.ipt_cantidad.setValidator(QIntValidator())

        self.btn_alta.clicked.connect(self.alta)
        self.btn_borrar.clicked.connect(self.borrar)
        self.btn_modificar.clicked.connect(self.modificar)
        self.btn_consultar.clicked.connect(self.consultar)
        self.btn_buscar.clicked.connect(self.buscar)
        # ancho 491
        self.table_widget.setColumnWidth(0, 50)
        self.table_widget.setColumnWidth(1, 200)
        self.table_widget.setColumnWidth(2, 100)
        self.table_widget.setColumnWidth(3, 100)

        self.numcolums = 4

        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def alta(
        self,
    ):
        """Función asociada al click del boton Alta para efecutar la persistencia del producto en el modelo."""
        nombre = self.ipt_nombre.text()
        cantidad = self.ipt_cantidad.text()
        precio = self.ipt_precio.text()

        try:
            id = self.controller.alta(nombre, cantidad, precio)

            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            self.table_widget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(id))
            )
            self.table_widget.setItem(
                row_position, 1, QtWidgets.QTableWidgetItem(str(nombre))
            )
            self.table_widget.setItem(
                row_position, 2, QtWidgets.QTableWidgetItem(cantidad)
            )
            self.table_widget.setItem(
                row_position, 3, QtWidgets.QTableWidgetItem(precio)
            )

            continuar = QMessageBox.information(
                self,
                "Alta Producto",
                "El producto se dio de alta satisfactoriamente",
                QMessageBox.Ok,
            )
        except Exception as e:
            continuar = QMessageBox.critical(
                self, "Alta Producto", f"{e}", QMessageBox.Ok
            )

    def consultar(
        self,
    ):
        """Función asociada al click del boton Consultar para efecutar la carga de productos del modelo en la grilla."""
        try:
            lista_prod = self.controller.get_productos()

            if len(lista_prod) == 0:
                continuar = QMessageBox.information(
                    self,
                    "Consultar Producto",
                    "No se han encontrado productos.",
                    QMessageBox.Ok,
                )
                return

            numrows = len(lista_prod)
            numcols = len(lista_prod[0])

            self.table_widget.setColumnCount(numcols)
            self.table_widget.setRowCount(numrows)

            for row in range(numrows):
                for column in range(numcols):
                    self.table_widget.setItem(
                        row,
                        column,
                        QtWidgets.QTableWidgetItem(str(lista_prod[row][column])),
                    )
        except Exception as e:
            continuar = QMessageBox.critical(
                self, "Alta Producto", f"{e}", QMessageBox.Ok
            )
            return

        continuar = QMessageBox.information(
            self,
            "Consultar Producto",
            f"Se han encontrado {len(lista_prod)} productos.",
            QMessageBox.Ok,
        )

    def borrar(
        self,
    ):
        """Función asociada al click del boton Borrar para efecutar el borrado del producto seleccionado en la grilla."""
        indexes = self.table_widget.selectionModel().selectedRows()

        if len(indexes) == 0:
            continuar = QMessageBox.information(
                self,
                "Borrar Producto",
                "Para borrar un producto primero debe seleccionar un registro de la grilla",
                QMessageBox.Ok,
            )
            return

        if len(indexes) > 1:
            continuar = QMessageBox.question(
                self,
                "Borrar Producto",
                f"Ha seleccionado {len(indexes)} producto.\n ¿Esta seguro que desea borrarlos todos?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if continuar == QMessageBox.No:
                return

        if len(indexes) == 1:
            continuar = QMessageBox.question(
                self,
                "Borrar Producto",
                "¿Esta seguro que desea borrar el producto seleccionado?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if continuar == QMessageBox.No:
                return

        offset = 0

        for index in sorted(indexes):
            try:
                id = self.controller.borrar(index.row() - offset)
                offset += 1
            except Exception as e:
                continuar = QMessageBox.critical(
                    self, "Borrar Producto", f"{e}", QMessageBox.Ok
                )
                return

        offset = 0
        for index in sorted(indexes):
            try:
                self.table_widget.removeRow(index.row() - offset)
                offset += 1
            except Exception as e:
                continuar = QMessageBox.critical(
                    self, "Borrar Producto", f"{e}", QMessageBox.Ok
                )
                return

        continuar = QMessageBox.information(
            self,
            "Borrar Producto",
            "El/los productos seleccionado/s se borraron satisfactoriamente",
            QMessageBox.Ok,
        )

    def modificar(
        self,
    ):
        """Función asociada al click del boton Modificar para invocar la pantalla de modificacion de productos según el seleccionado en la grilla."""
        indexes = self.table_widget.selectionModel().selectedRows()

        if len(indexes) == 0:
            continuar = QMessageBox.information(
                self,
                "Modificar Producto",
                "Para modificar un producto primero debe seleccionarlo haciendo click sobre el margen izquierdo de la fila",
                QMessageBox.Ok,
            )
            return

        if len(indexes) > 1:
            continuar = QMessageBox.critical(
                self,
                "Modificar Producto",
                f"Ha seleccionado {len(indexes)} productos.\n Solo puede modificar uno por vez",
                QMessageBox.Ok,
            )
            return

        try:
            prod = self.controller.get_producto_por_index(indexes[0].row())
        except Exception as e:
            continuar = QMessageBox.critical(
                self, "Modificar Producto", f"{e}", QMessageBox.Ok
            )
            return

        pop_modif = ModProdWindow(prod, self)
        prod_modif = pop_modif.launch()

        if prod_modif is None:
            return
        try:
            self.controller.actualizar_producto(indexes[0].row(), prod_modif)
            if prod_modif is not None:
                self.table_widget.setItem(
                    indexes[0].row(), 0, QtWidgets.QTableWidgetItem(str(prod_modif.id))
                )
                self.table_widget.setItem(
                    indexes[0].row(),
                    1,
                    QtWidgets.QTableWidgetItem(str(prod_modif.nombre)),
                )
                self.table_widget.setItem(
                    indexes[0].row(),
                    2,
                    QtWidgets.QTableWidgetItem(str(prod_modif.cantidad)),
                )
                self.table_widget.setItem(
                    indexes[0].row(),
                    3,
                    QtWidgets.QTableWidgetItem(str(prod_modif.precio)),
                )

            continuar = QMessageBox.information(
                self,
                "Modificar Producto",
                "El producto seleccionado se ha modificado satisfactoriamente",
                QMessageBox.Ok,
            )
        except Exception as e:
            continuar = QMessageBox.critical(
                self, "Modificar Producto", f"{e}", QMessageBox.Ok
            )
            return

    def buscar(
        self,
    ):
        """Función asociada al click del boton Buscar para invocar la pantalla de busqueda de productos."""
        try:
            pop_buscar = BuscarProdWindow(self, self.controller)
            pop_buscar.setFixedHeight(150)
            pop_buscar.setFixedWidth(250)
            prod_find = pop_buscar.launch()

            if prod_find is None:
                return

            self.table_widget.setRowCount(0)

            numrows = len(prod_find)
            numcols = len(prod_find[0])
            self.table_widget.setColumnCount(numcols)
            self.table_widget.setRowCount(numrows)

            for row in range(numrows):
                for column in range(numcols):
                    self.table_widget.setItem(
                        row,
                        column,
                        QtWidgets.QTableWidgetItem(str(prod_find[row][column])),
                    )

            continuar = QMessageBox.information(
                self,
                "Buscar Producto",
                f"Se han encontrado {len(prod_find)} productos.",
                QMessageBox.Ok,
            )
        except Exception as e:
            continuar = QMessageBox.critical(
                self, "Buscar Producto", f"{e}", QMessageBox.Ok
            )
            return
