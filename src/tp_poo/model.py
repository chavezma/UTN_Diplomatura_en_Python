import sqlite3
import re
import traceback
import sys

# ##############################################
# MODELO
# ##############################################

class Model():
    def __init__(self, ):
        self.con = self.conexion()
        self.crear_tabla()

    def conexion(self,):
        return sqlite3.connect("mibase.db")

    def crear_tabla(self):
        cursor = self.con.cursor()

        sql = """ CREATE TABLE IF NOT EXISTS productos
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    producto varchar(20) NOT NULL,
                    cantidad real,
                    precio real
                )
        """
        cursor.execute(sql)
        self.con.commit()

    def getProductos(self,):
        try:
            sql = "SELECT * FROM productos ORDER BY id DESC"
            self.con = self.conexion()
            cursor = self.con.cursor()
            datos = cursor.execute(sql)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar seleccionar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += 'Printing detailed SQLite exception traceback: ' + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception('Error: ', message)
        finally:
            self.con.commit()

        return datos.fetchall()

    def alta(self, producto, cantidad, precio):
        cadena = producto
        patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena

        if (not re.match(patron, cadena)):
            return False

        try:
            cursor = self.con.cursor()
            data = (producto, cantidad, precio)
            sql = "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar insertar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += 'Printing detailed SQLite exception traceback: ' + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception('Error: ', message)
        finally:
            self.con.commit()

        return True

    def borrar(self, id):
        try:
            cursor = self.con.cursor()
            el_id = int(id)
            data = (el_id,)
            sql = "DELETE from productos where id = ?;"
            cursor.execute(sql, data)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar borrar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += 'Printing detailed SQLite exception traceback: ' + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception('Error: ', message)
        finally:
            self.con.commit()

        return True

    def actualizar(self, id, producto, cantidad, precio):
        try:
            cursor = self.con.cursor()
            prod_id = int(id)
            data = (producto, cantidad, precio, prod_id)
            sql = "UPDATE productos SET producto=?, cantidad=?, precio=? WHERE id=?;"
            cursor.execute(sql, data)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar actualizar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += 'Printing detailed SQLite exception traceback: ' + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception('Error: ', message)
        finally:
            self.con.commit()

        return True
