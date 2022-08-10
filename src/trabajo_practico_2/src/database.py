from ast import Raise
import sys
import os
import sqlite3
import traceback
from datetime import datetime

from singleton import Singleton

flog = None

def loguear_transaccion(f):
    """Decorador para realizar un trace de las transacciones de base de datos realizadas durante una sesion.
    """
    print("Entrando a loguear")

    global flog

    def wrapper(*args, **kwargs):
        start = datetime.now()
        try:
            res = f(*args, **kwargs)
            end = datetime.now()
        except Exception as exc:
            end = datetime.now()
            flog.write(f"Called [{f.__name__}] with {args} at {start} - duration {end - start} with error [{exc}]\n")
            flog.flush()
            raise Exception(exc)

        flog.write(f"Called [{f.__name__}] with {args} at {start} - duration {end - start}\n")
        flog.flush()
        return res

    return wrapper

@Singleton
class Database:
    """Clase que encapsula la interacción entre el :class: ´Producto´ y su persistencia en la BD sqllite
    Solo se permite una sola instancia.
    """

    def __init__(
        self,
    ):
        self.__con = self.__conexion()
        self.__crear_tabla()
        cursor = self.__con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("PRAGMA integrity_check;")
        global flog
        flog = open("logfile.txt", "a")

    def __conexion(
        self,
    ):
        """Genera una conexión con la base de datos

        :return: id de producto que se acaba de generar
        :rtype: :class: ´sqlite3.Connection´
        """
        return sqlite3.connect(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "Productos.db")
        )

    def __crear_tabla(
        self,
    ):
        """Genera el modelo de datos (tablas) si no existen."""
        cursor = self.__con.cursor()

        sql = """ CREATE TABLE IF NOT EXISTS productos
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre varchar(20) NOT NULL,
                    cantidad real NOT NULL,
                    precio real NOT NULL,
                    UNIQUE(nombre)
                )
        """
        cursor.execute(sql)
        self.__con.commit()

    @loguear_transaccion
    def get_many_products(
        self,
    ):
        """Realiza la consulta a la base de datos para obtener todos los registros de la tabla ´productos´

        :return: Listado de productos cargados en forma de tuplas
        :rtype: list(tuple)
        """
        try:
            sql = "SELECT * FROM productos ORDER BY id ASC"
            cursor = self.__con.cursor()
            datos = cursor.execute(sql)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar obtener los productos\n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += "Detalle SQLite exception traceback: " + "\n"

            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception(f"Error: {message}")
        finally:
            self.__con.commit()

        return datos.fetchall()

    @loguear_transaccion
    def insert(
        self,
        prod,
    ):
        """Realiza la inserción del producto ´prod´ a la base de datos

        :param prod: Objeto con la información del producto que se quiere insertar
        :type prod: Producto
        :return: El id del objeto que se acaba de insertar
        :rtype: int
        """
        try:
            cursor = self.__con.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            cursor.execute("PRAGMA integrity_check;")

            data = (prod.nombre, prod.cantidad, prod.precio)

            sql = "INSERT INTO productos(nombre, cantidad, precio) VALUES(?, ?, ?)"
            datos = cursor.execute(sql, data)
        except sqlite3.IntegrityError as error:
            raise Exception(
                "Error: El nombre ya esta siendo utilizado por otro producto"
            )
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar insertar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += "Detalle SQLite exception traceback: " + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)

            raise Exception(f"Error: {message}")
        except Exception as error:
            message = "sqllite: Ocurrió un error al intentar insertar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += "Detalle SQLite exception traceback: " + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception(f"Error: {message}")

        self.__con.commit()
        return cursor.lastrowid

    @loguear_transaccion
    def delete(
        self,
        prod,
    ):
        """Realiza el borrado del producto ´prod´ a la base de datos

        :param prod: Objeto con la información del producto que se quiere borrar
        :type prod: Producto
        """
        try:
            cursor = self.__con.cursor()
            data = (int(prod.id),)
            sql = "DELETE from productos where id = ?;"
            cursor.execute(sql, data)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar borrar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += "Detalle SQLite exception traceback: " + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception(f"Error: {message}")
        finally:
            self.__con.commit()

    @loguear_transaccion
    def update(
        self,
        prod,
    ):
        """Realiza la actualizacion del producto ´prod´ a la base de datos

        :param prod: Objeto con la información del producto que se quiere actualizar
        :type prod: Producto
        """
        try:
            cursor = self.__con.cursor()
            data = (prod.nombre, prod.cantidad, prod.precio, int(prod.id))
            sql = "UPDATE productos SET nombre=?, cantidad=?, precio=? WHERE id=?;"
            cursor.execute(sql, data)
        except sqlite3.IntegrityError as error:
            raise Exception(
                "Error: El nombre ya esta siendo utilizado por otro producto"
            )
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar actualizar \n"
            message += "Exception class is: " + error.__class__ + "\n"
            message += "Exception is " + error.args + "\n"
            message += "Detalle SQLite exception traceback: " + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += traceback.format_exception(exc_type, exc_value, exc_tb)
            raise Exception(f"Error: {message}")
        finally:
            self.__con.commit()

    @loguear_transaccion
    def find_products(
        self,
        nombre,
        condicion,
    ):
        """Dado un nombre y una condicion, realiza la busqueda en la base de datos.

        :param nombre: Nombre o parte del nombre del producto que se desea buscar.
        :type nombre: str
        :param condicion: Valores que indican el tipo de filtro a usar ´Empieza con´, ´Termina con´ o ´Contiene´
        :type condicion: str
        :return: Listado de productos cargados en forma de tuplas
        :rtype: list
        """
        try:
            cursor = self.__con.cursor()
            if condicion == "Comienza con":
                data = (f"{nombre}%",)
            elif condicion == "Termina con":
                data = (f"%{nombre}",)
            else:  # CONTIENE
                data = (f"%{nombre}%",)

            sql = "SELECT * FROM productos where nombre like ?"
            datos = cursor.execute(sql, data)
        except sqlite3.Error as error:
            message = "sqllite: Ocurrió un error al intentar buscar \n"
            message += "Exception class is: " + str(error.__class__) + "\n"
            message += "Exception is " + str(error.args) + "\n"
            message += "Detalle SQLite exception traceback: " + "\n"
            exc_type, exc_value, exc_tb = sys.exc_info()
            message += str(traceback.format_exception(exc_type, exc_value, exc_tb))
            raise Exception(f"Error: {message}")
        finally:
            self.__con.commit()

        return datos.fetchall()
