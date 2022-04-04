import sqlite3
from types import NoneType
import init_db as db
import sys
import traceback

# ---------------------------------------------------------------------------------------------------------
# TABLA USUARIOS
# ---------------------------------------------------------------------------------------------------------
def usuario_login(con, email, contrasenia):
    cursor = con.cursor()
    data = (email, contrasenia)
    sql = "SELECT * FROM usuarios WHERE email =? and contrasenia =?"
    cursor.execute(sql, data)
    row = cursor.fetchone()

    if row is None or row is NoneType:
        return None
    else:
        return dict(row)


def usuario_insertar(con, nombre, apellido, email, fecha_nacimiento, contrasenia):
    cursor = con.cursor()
    data = (nombre, apellido, email, fecha_nacimiento, contrasenia)
    sql = "INSERT INTO usuarios(nombre, apellido, email, fecha_nacimiento, contrasenia) VALUES(?, ?, ?, ?, ?)"
    cursor.execute(sql, data)
    con.commit()


def usuario_actualizar(con, id, nombre, apellido, email, fecha_nacimiento, contrasenia):
    cursor = con.cursor()
    mi_id = int(id)
    data = (nombre, apellido, email, fecha_nacimiento, contrasenia, mi_id)
    sql = "UPDATE usuarios SET nombre=?, apellido=?, email=?, fecha_nacimiento=?, contrasenia=? WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()


def usuario_borrar(con, id):
    cursor = con.cursor()
    mi_id = int(id)
    data = (mi_id,)
    sql = "DELETE from usuarios where id = ?;"
    cursor.execute(sql, data)
    con.commit()


def usuario_seleccionar(con, id):
    dict_usuarios = {}
    cursor = con.cursor()
    mi_id = int(id)
    data = (mi_id,)
    sql = "SELECT * FROM usuarios WHERE id =?;"
    cursor.execute(sql, data)
    row = cursor.fetchone()
    return dict(row)


# ---------------------------------------------------------------------------------------------------------
# TABLA PROYECTOS
# ---------------------------------------------------------------------------------------------------------


def proyecto_insertar(con, nombre, descripcion, usuario_id):
    cursor = con.cursor()
    data = (nombre, descripcion, usuario_id)
    sql = "INSERT INTO proyectos(nombre, descripcion, usuario_id) VALUES(?, ?, ?)"
    cursor.execute(sql, data)
    pry_id = cursor.lastrowid
    con.commit()

    return pry_id


def proyecto_actualizar(con, id, nombre, descripcion):
    cursor = con.cursor()
    mi_id = int(id)
    data = (nombre, descripcion, mi_id)
    sql = "UPDATE proyectos SET nombre=?, descripcion=? WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()

def proyecto_borrar(con, id):
    cursor = con.cursor()
    mi_id = int(id)
    data = (mi_id,)
    sql = "DELETE from proyectos where id = ?;"
    cursor.execute(sql, data)
    con.commit()

def proyecto_seleccionar(con, usr_id, pry_id=None):
    cursor = con.cursor()
    mi_user_id = int(usr_id)

    if pry_id is None:
        data = (mi_user_id,)
        sql = "SELECT * FROM proyectos WHERE usuario_id =?;"
    else:
        mi_id = int(pry_id)
        data = (
            mi_id,
            mi_user_id,
        )
        sql = "SELECT * FROM proyectos WHERE id =? AND usuario_id =?"

    cursor.execute(sql, data)
    row = cursor.fetchall()

    result = {}
    for r in row:
        temp = dict(r)
        result[temp["id"]] = temp

    return result


# ---------------------------------------------------------------------------------------------------------
# TABLA ARCHIVOS
# ---------------------------------------------------------------------------------------------------------


def archivo_insertar(con, proyecto_id, nombre_archivo, ruta_archivo):
    cursor = con.cursor()
    data = (proyecto_id, nombre_archivo, ruta_archivo)
    sql = "INSERT INTO archivos_x_proyecto(proyecto_id, nombre_archivo, ruta_archivo) VALUES(?, ?, ?)"
    cursor.execute(sql, data)
    arch_id = cursor.lastrowid
    con.commit()

    return arch_id


def archivo_actualizar(con, id, nombre_archivo, ruta_archivo):
    cursor = con.cursor()
    mi_id = int(id)
    data = (nombre_archivo, ruta_archivo, mi_id)
    sql = "UPDATE archivos_x_proyecto SET nombre_archivo=?, ruta_archivo=? WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()


def archivo_borrar(con, id):
    cursor = con.cursor()
    mi_id = int(id)
    data = (mi_id,)
    sql = "DELETE from archivos_x_proyecto where id = ?;"
    cursor.execute(sql, data)
    con.commit()


def archivo_seleccionar(con, pry_id, arch_id=None):
    cursor = con.cursor()
    mi_pry_id = int(pry_id)

    if arch_id is None:
        data = (mi_pry_id,)
        sql = "SELECT * FROM archivos_x_proyecto WHERE proyecto_id =?;"
    else:
        mi_arch_id = int(arch_id)
        data = (
            mi_arch_id,
            mi_pry_id,
        )
        sql = "SELECT * FROM archivos_x_proyecto WHERE id =? AND proyecto_id =?"

    cursor.execute(sql, data)
    row = cursor.fetchall()

    result = {}
    for r in row:
        temp = dict(r)
        result[temp["id"]] = temp

    return result


if __name__ == "__main__":
    con = db.conectar()
    con.row_factory = sqlite3.Row
