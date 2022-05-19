import sqlite3
import re

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
        sql = "SELECT * FROM productos ORDER BY id DESC"
        self.con = self.conexion()
        cursor = self.con.cursor()
        datos = cursor.execute(sql)

        return datos.fetchall()

    def alta(self, producto, cantidad, precio):
        print("modelo.alta")
        cadena = producto
        patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena

        if (not re.match(patron, cadena)):
            print("error en campo producto")
            return False

        print("modelo.alta.sql")
        print(producto, cantidad, precio)
        try:
            cursor = self.con.cursor()
            data = (producto, cantidad, precio)
            sql = "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
        except Exception as err:
            print('Alta Failed: %s\nError: %s' % (sql, str(err)))
        finally:
            self.con.commit()

        print("modelo.alta.fin")
        return True

    def borrar(self, id):
        try:
            cursor = self.con.cursor()
            el_id = int(id)
            data = (el_id,)
            sql = "DELETE from productos where id = ?;"
            cursor.execute(sql, data)
        except Exception as err:
            print('Borrar Failed: %s\nError: %s' % (sql, str(err)))
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
        except Exception as err:
            print('Actualizar Failed: %s\nError: %s' % (sql, str(err)))
        finally:
            self.con.commit()

        return True
