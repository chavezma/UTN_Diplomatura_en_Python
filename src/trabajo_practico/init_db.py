import sqlite3


def conectar():
    con = sqlite3.connect(".\\transferX.db")
    return con

def crear_tabla_usuario(db_con):
    cursor = con.cursor()
    sql = "CREATE TABLE usuarios(id integer PRIMARY KEY, nombre text, apellido text, fecha_nacimiento date, contrasenia text, email text)"
    cursor.execute(sql)
    con.commit()

def crear_tabla_proyectos(db_con):
    cursor = con.cursor()
    sql = "CREATE TABLE proyectos(id integer PRIMARY KEY, nombre text, descripcion text, usuario_id integer, FOREIGN KEY(usuario_id) REFERENCES usuarios(id) )"
    cursor.execute(sql)
    con.commit()

def crear_tabla_archivos(db_con):
    cursor = con.cursor()
    sql = "CREATE TABLE archivos_x_proyecto(id integer PRIMARY KEY, proyecto_id integer, nombre_archivo text, ruta_archivo text, FOREIGN KEY(proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE)"
    cursor.execute(sql)
    con.commit()

if __name__ == "__main__":
    con = conectar()
    crear_tabla_usuario(con)
    crear_tabla_proyectos(con)
    crear_tabla_archivos(con)
