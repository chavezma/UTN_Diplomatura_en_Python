import os
import re
import binascii
import sqlite3
from datetime import datetime
from tkinter.messagebox import showerror, showinfo, askyesno
import init_db as db
from database import (
    usuario_login, usuario_insertar, usuario_actualizar,
    proyecto_seleccionar, proyecto_insertar, proyecto_borrar, proyecto_actualizar,
    archivo_seleccionar, archivo_insertar, archivo_borrar, archivo_actualizar
)
from menu_ayuda import fn_sobre
from tkinter.ttk import Separator, Notebook, Treeview, Combobox, Scrollbar
from tkinter import (BOTH, CENTER, HORIZONTAL, VERTICAL, LEFT, RIGHT, TOP, E, W, NO, Button, Entry, Label, StringVar, Tk, Toplevel, font, X, Menu, Frame)

db_con = None
app_usuario = None
scr_app = Tk()
lbl_fuente = font.Font(weight="bold")
notebook = Notebook(scr_app)
frm_proyecto = Frame(notebook, width=450, height=450)
frm_archivo = Frame(notebook, width=450, height=450)

def reset_user(nombre, apellido, email, fecha_nacimiento, contrasenia):
    usuario_actualizado = get_user()
    usuario_actualizado["nombre"] = nombre
    usuario_actualizado["apellido"] = apellido
    usuario_actualizado["email"] = email
    usuario_actualizado["fecha_nacimiento"] = fecha_nacimiento
    usuario_actualizado["contrasenia"] = contrasenia
    set_user(usuario_actualizado)

def set_user(usuario):
    app_usuario = usuario
    hexStr = binascii.hexlify(str(usuario).encode())
    f = open("temp", "wb", 0)
    f.write(hexStr)
    f.flush()
    f.close()

def get_user():
    try:
        f = open("temp", "rb")
        data = f.read()
        f.close()
        return eval(binascii.unhexlify(data.decode()))
    except FileNotFoundError:
        # print("File does not exist")git s
        return None

def validar_usuario(nombre, apellido, email, fecha_nacimiento, contrasenia):

    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex_fecha = '^(?:(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9]))/[0-9]{4}$'

    if nombre.strip() == "" or apellido.strip() == "" or email.strip() == "" or fecha_nacimiento.strip() == "" or contrasenia.strip() == "":
        showerror("Guardar Usuario", "Debe ingresar todos los campos para continuar...")
        return False

    if not re.search(regex_email, email):
        showerror("Guardar Usuario", f"El email ingresado [{email}] tiene un formato incorrecto...")
        return False

    if not re.search(regex_fecha, fecha_nacimiento):
        showerror("Guardar Usuario", f"La fecha ingresada [{fecha_nacimiento}] tiene un formato incorrecto. Se debe respetar DD/MM/YYYY")
        return False

    try:
        datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    except ValueError:
        showerror("Guardar Usuario", f"La fecha ingresada [{fecha_nacimiento}] tiene un formato incorrecto...")
        return False

    return True


def app_start(db_con):
    scr_app.geometry("550x400")
    scr_app.title("TransferX")
    scr_app.resizable(0, 0)
    config(db_con, scr_app)

    scr_app.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ACTUALIZAR USUARIO
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def fn_usr_actualizar(con, id, nombre, apellido, email, fecha_nacimiento, contrasenia, pantalla):
    global lbl_str_conectado

    if validar_usuario(nombre, apellido, email, fecha_nacimiento, contrasenia):
        if askyesno("Actualizar", "Esta seguro que desea actualizar los datos de usuario?"):
            usuario_actualizar(con, id, nombre, apellido, email, fecha_nacimiento, contrasenia)
            showinfo("Guardar Usuario", "El usuario ha sigo actualizado exitosamente.")
            lbl_str_conectado.set("Conectado: " + email)
            reset_user(nombre, apellido, email, fecha_nacimiento, contrasenia)
            pantalla.destroy()

def fn_scr_usr_modificar(db_con, scr):
    usuario_logueado = get_user()
    scr_usr_modificar = Toplevel(scr)
    scr_usr_modificar.title("Modificar usuario")
    scr_usr_modificar.geometry("400x650")
    scr_usr_modificar.grab_set()
    scr_usr_modificar.resizable(0, 0)

    def fn_antes_cerrar():
        scr_usr_modificar.grab_set()
        scr_usr_modificar.destroy()

    scr_usr_modificar.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    lbl_fuente = font.Font(weight="bold")
    var_nombre = StringVar()
    var_apellido = StringVar()
    var_email = StringVar()
    var_fecha_nacimiento = StringVar()
    var_contrasenia = StringVar()

    var_nombre.set(usuario_logueado["nombre"])
    var_apellido.set(usuario_logueado["apellido"])
    var_email.set(usuario_logueado["email"])
    var_fecha_nacimiento.set(usuario_logueado["fecha_nacimiento"])
    var_contrasenia.set(usuario_logueado["contrasenia"])

    lbl_nombre = Label(scr_usr_modificar, text="Nombre:", font=lbl_fuente)
    lbl_apellido = Label(scr_usr_modificar, text="Apellido:", font=lbl_fuente)
    lbl_email = Label(scr_usr_modificar, text="Email:", font=lbl_fuente)
    lbl_fecha_nacimiento = Label(scr_usr_modificar, text="Fecha Nacimiento:", font=lbl_fuente)
    lbl_contrasenia = Label(scr_usr_modificar, text="Contraseña:", font=lbl_fuente)

    ipt_nombre = Entry(scr_usr_modificar, textvariable=var_nombre, width=25)
    ipt_apellido = Entry(scr_usr_modificar, textvariable=var_apellido, width=25)
    ipt_email = Entry(scr_usr_modificar, textvariable=var_email, width=25)
    ipt_fecha_nacimiento = Entry(scr_usr_modificar, textvariable=var_fecha_nacimiento, width=25)
    ipt_contrasenia = Entry(scr_usr_modificar, textvariable=var_contrasenia, width=25)

    btn_guardar = Button(
        scr_usr_modificar,
        text="Modificar",
        height=2,
        width=15,
        command=lambda: fn_usr_actualizar(
            db_con,
            usuario_logueado["id"],
            var_nombre.get(),
            var_apellido.get(),
            var_email.get(),
            var_fecha_nacimiento.get(),
            var_contrasenia.get(),
            scr_usr_modificar,
        ),
    )

    btn_cancelar = Button(scr_usr_modificar, text="Cancelar", height=2, width=15, command=fn_antes_cerrar)

    btn_guardar.place(rely=0.5, anchor=CENTER)
    btn_cancelar.place(rely=0.5, anchor=CENTER)
    separ1 = Separator(scr_usr_modificar, orient=HORIZONTAL)

    lbl_nombre.grid(row=1, column=1)
    ipt_nombre.grid(row=1, column=2)
    lbl_apellido.grid(row=2, column=1)
    ipt_apellido.grid(row=2, column=2)
    lbl_email.grid(row=3, column=1)
    ipt_email.grid(row=3, column=2)
    lbl_fecha_nacimiento.grid(row=4, column=1)
    ipt_fecha_nacimiento.grid(row=4, column=2)
    lbl_contrasenia.grid(row=5, column=1)
    ipt_contrasenia.grid(row=5, column=2)

    separ1.grid(row=6, columnspan=6, pady=5, sticky="ew")
    btn_guardar.grid(row=7, column=1)
    btn_cancelar.grid(row=7, column=2)

    # Indicamos que la ventana principal espere por la finalizacion del login.
    scr.wait_window(scr_usr_modificar)

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# REGISTRAR USUARIO
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def fn_usr_guardar(con, nombre, apellido, email, fecha_nacimiento, contrasenia, pantalla):

    if validar_usuario(nombre, apellido, email, fecha_nacimiento, contrasenia):
        usuario_insertar(con, nombre, apellido, email, fecha_nacimiento, contrasenia)
        showinfo("Guardar Usuario", "El usuario ha sigo guardado exitosamente.")
        pantalla.destroy()

def fn_usr_registrar(db_con, scr):
    scr_registrar = Toplevel(scr)
    scr_registrar.grab_set()
    scr_registrar.resizable(0, 0)

    def fn_antes_cerrar():
        scr_registrar.grab_set()
        scr_registrar.destroy()

    scr_registrar.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    lbl_fuente = font.Font(weight="bold")
    scr_registrar.grab_set()
    scr_registrar.title("Registrar usuario")
    scr_registrar.geometry("325x175")

    var_nombre = StringVar()
    var_apellido = StringVar()
    var_email = StringVar()
    var_fecha_nacimiento = StringVar()
    var_contrasenia = StringVar()

    lbl_nombre = Label(scr_registrar, text="Nombre:", font=lbl_fuente)
    lbl_apellido = Label(scr_registrar, text="Apellido:", font=lbl_fuente)
    lbl_email = Label(scr_registrar, text="Email:", font=lbl_fuente)
    lbl_fecha_nacimiento = Label(scr_registrar, text="Fecha Nacimiento:", font=lbl_fuente)
    lbl_contrasenia = Label(scr_registrar, text="Contraseña:", font=lbl_fuente)

    ipt_nombre = Entry(scr_registrar, textvariable=var_nombre, width=25)
    ipt_apellido = Entry(scr_registrar, textvariable=var_apellido, width=25)
    ipt_email = Entry(scr_registrar, textvariable=var_email, width=25)
    ipt_fecha_nacimiento = Entry(scr_registrar, textvariable=var_fecha_nacimiento, width=25)
    ipt_contrasenia = Entry(scr_registrar, textvariable=var_contrasenia, width=25, show="*")

    btn_guardar = Button(
        scr_registrar,
        text="Guardar",
        height=1,
        width=15,
        command=lambda: fn_usr_guardar(
            db_con,
            var_nombre.get(),
            var_apellido.get(),
            var_email.get(),
            var_fecha_nacimiento.get(),
            var_contrasenia.get(),
            scr_registrar,
        ),
    )

    btn_cancelar = Button(scr_registrar, text="Cancelar", height=1, width=15, command=fn_antes_cerrar)

    separ1 = Separator(scr_registrar, orient=HORIZONTAL)

    lbl_nombre.grid(row=1, column=1)
    ipt_nombre.grid(row=1, column=2)
    lbl_apellido.grid(row=2, column=1)
    ipt_apellido.grid(row=2, column=2)
    lbl_email.grid(row=3, column=1)
    ipt_email.grid(row=3, column=2)
    lbl_fecha_nacimiento.grid(row=4, column=1)
    ipt_fecha_nacimiento.grid(row=4, column=2)
    lbl_contrasenia.grid(row=5, column=1)
    ipt_contrasenia.grid(row=5, column=2)

    separ1.grid(row=6, columnspan=6, pady=5, sticky="ew")
    btn_guardar.grid(row=7, column=1)
    btn_cancelar.grid(row=7, column=2)

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# LOGIN
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
def fn_ingresar(con, scr, usuario, clave):

    if usuario.strip() == "" or clave.strip() == "":
        showerror("Ingreso", "Faltan completar campos para validar el ingreso a la aplicación.")

    user = usuario_login(con, usuario, clave)

    if user is None:
        showerror("Ingreso", "Las credenciales informadas son inválidas")
    else:
        set_user(user)
        scr.destroy()

def fn_login(db_con, scr_app):
    scr_login = Toplevel(scr_app)
    scr_login.resizable(0, 0)
    scr_login.geometry("400x250")
    scr_login.title("Acceso al sistema")
    scr_login.grab_set()
    lbl_fuente = font.Font(weight="bold")

    def fn_antes_cerrar():
        scr_login.grab_set()
        scr_login.destroy()

    scr_login.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    usuario = StringVar()
    clave = StringVar()

    Label(scr_login, text="Ingrese sus credenciales para comenzar", font=("Calibri", 13)).pack()
    Label(scr_login, text="")

    lbl_user = Label(scr_login, text="Email:", font=lbl_fuente)
    lbl_pass = Label(scr_login, text="Contraseña:", font=lbl_fuente)

    input_user = Entry(scr_login, textvariable=usuario, width=25)
    input_pass = Entry(scr_login, textvariable=clave, width=25, show="*")

    btn_login = Button(
        scr_login,
        text="Ingresar",
        height=2,
        width=15,
        command=lambda: fn_ingresar(db_con, scr_login, usuario.get(), clave.get()),
    )

    btn_reg = Button(
        scr_login,
        text="Registrar",
        height=2,
        width=15,
        command=lambda: fn_usr_registrar(db_con, scr_login),
    )

    btn_login.place(rely=0.5, anchor=CENTER)
    btn_reg.place(rely=0.5, anchor=CENTER)
    separ1 = Separator(scr_login, orient=HORIZONTAL)

    lbl_user.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    input_user.pack(side=TOP, expand=False, padx=5, pady=5)
    lbl_pass.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    input_pass.pack(side=TOP, expand=False, padx=5, pady=5)

    separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    btn_login.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=6)
    btn_reg.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

    input_user.focus()

    # Indicamos que la ventana principal espere por la finalizacion del login.
    scr_app.wait_window(scr_login)

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# GESTION ARCHIVO
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def fn_tv_guardar_archivo(db_con, el_tv):
    if var_nombre.get().strip() == "" or var_ruta.get().strip() == "":
        showerror("Guardar Archivo", "Para guardar debe ingresar información del archivo.")
        ipt_nombre.focus()
        return

    actual_proyecto = box_value.get().split()[0]

    arch_id = archivo_insertar(db_con, actual_proyecto, var_nombre.get(), var_ruta.get())

    if arch_id is not None and arch_id != "":
        showinfo("Guardar Archivo", "El archivo fue guardado correctamente.")
        var_nombre.set("")
        var_ruta.set("")

def fn_tv_borrar_archivo(db_con, el_treeview):
    item = el_treeview.focus()

    if item is None or item == "":
        showerror("Borrar Archivo", "Para borrar un archivo debe seleccionarlo previamente.")
        return

    arch_id = el_treeview.item(item)["text"]

    if askyesno("Borrar Archivo", "¿Está seguro que desea borrar el archivo?"):
        archivo_borrar(db_con, arch_id)
        showinfo("Borrar Archivo", "El archivo fue borrado correctamente.")
        el_treeview.delete(item)

def fn_scr_pry_guardar_archivo(db_con, nombre, ruta, el_tv, scr):
    el_arch = el_tv.focus()

    if el_arch is None or el_arch == "":
        showerror("Actualizar Archivo", "Para actualizar un archivo debe seleccionarlo previamente.")
        return

    arch_id = el_tv.item(el_arch)["text"]
    if askyesno("Actualizar Archivo", "¿Está seguro que desea actualizar el archivo?"):
        archivo_actualizar(db_con, arch_id, nombre, ruta)
        showinfo("Actualizar Archivo", "El archivo fue actualizado correctamente.")
        el_tv.item(el_arch, values=(nombre, ruta))
        scr.destroy()

def fn_scr_actualizar_archivo(db_con, scr, el_arch_tv):
    scr_act_archivo = Toplevel(scr)
    scr_act_archivo.resizable(0, 0)
    scr_act_archivo.title("Modificar Archivo")
    scr_act_archivo.geometry("400x250")
    scr_act_archivo.grab_set()
    lbl_fuente = font.Font(weight="bold")

    el_arch = el_arch_tv.focus()
    el_arch_nombre = el_arch_tv.item(el_arch)["values"][0]
    el_arch_ruta = el_arch_tv.item(el_arch)["values"][1]

    def fn_antes_cerrar():
        scr_act_archivo.grab_set()
        scr_act_archivo.destroy()

    scr_act_archivo.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    var_nombre = StringVar()
    var_ruta = StringVar()

    var_nombre.set(el_arch_nombre)
    var_ruta.set(el_arch_ruta)

    lbl_nombre = Label(scr_act_archivo, text="Nombre:", font=lbl_fuente)
    lbl_ruta = Label(scr_act_archivo, text="Ruta:", font=lbl_fuente)

    ipt_nombre = Entry(scr_act_archivo, textvariable=var_nombre, width=25)
    ipt_ruta = Entry(scr_act_archivo, textvariable=var_ruta, width=25)

    btn_arch_guardar = Button(
        scr_act_archivo,
        text="Guardar",
        height=2,
        width=15,
        command=lambda: fn_scr_pry_guardar_archivo(
            db_con,
            var_nombre.get(),
            var_ruta.get(),
            el_arch_tv,
            scr_act_archivo
        ),
    )

    btn_arch_cancelar = Button(scr_act_archivo, text="Cancelar", height=2, width=15, command=fn_antes_cerrar)

    btn_arch_guardar.place(rely=0.5, anchor=CENTER)
    btn_arch_cancelar.place(rely=0.5, anchor=CENTER)
    separ1 = Separator(scr_act_archivo, orient=HORIZONTAL)

    lbl_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    ipt_nombre.pack(side=TOP, expand=False, padx=5, pady=5)
    lbl_ruta.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    ipt_ruta.pack(side=TOP, expand=False, padx=5, pady=5)

    separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    btn_arch_guardar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=6)
    btn_arch_cancelar.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

    scr.wait_window(scr_act_archivo)

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# GESTION PROYECTO
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def fn_cargar_proyectos(con, id):
    global tv_proyecto_grid
    usuario_logueado = get_user()

    dict_proyectos = proyecto_seleccionar(con, usuario_logueado["id"], id)

    for key, valores in dict_proyectos.items():
        tv_proyecto_grid.insert("", index="end", text=key, values=(valores["nombre"], valores["descripcion"]))

def fn_tv_guardar_proyecto(db_con, el_tv):

    if var_titulo.get().strip() == "" or var_descripcion.get().strip() == "":
        showerror("Guardar Proyecto", "No se puede guardar un proyecto con campos nulos...")
        return

    usuario_logueado = get_user()
    pry_id = proyecto_insertar(db_con, var_titulo.get(), var_descripcion.get(), usuario_logueado["id"])

    if pry_id is not None:
        showinfo("Guardar Proyecto", "El proyecto fue guardado correctamente")
        el_tv.insert("", index="end", text=pry_id, values=(var_titulo.get(), var_descripcion.get()))
        var_titulo.set("")
        var_descripcion.set("")

def fn_tv_borrar_proyecto(db_con, el_treeview):

    item = el_treeview.focus()

    if item is None or item == "":
        showerror("Borrar Proyecto", "Para borrar debe seleccionar antes un proyecto de la grilla.")
        return

    if not askyesno("Borrar Proyecto", "¿Está seguro que desea borrar el proyecto seleccionado?"):
        return

    pry_id = el_treeview.item(item)["text"]

    dict_arch = archivo_seleccionar(db_con, pry_id)

    if len(dict_arch) > 0:
        if not askyesno("Borrar Proyecto", "El proyecto tiene archivos asociados ¿Desea continuar?"):
            return

    proyecto_borrar(db_con, pry_id)
    showinfo("Borrar Proyecto", "El proyecto ha sido borrado correctamente.")
    el_treeview.delete(item)

def fn_scr_pry_guardar_proyecto(db_con, titulo, descripcion, el_tv, scr):
    el_pry = el_tv.focus()

    if el_pry is None or el_pry == "":
        showerror("Actualizar Proyecto", "Para actualizar un proyecto debe seleccionar alguno de la grilla o hacer doble click sobre el mismo.")
        return

    if askyesno("Actualizar Proyecto", "¿Está seguro que desea actualizar el proyecto seleccionado?"):
        pry_id = el_tv.item(el_pry)["text"]
        proyecto_actualizar(db_con, pry_id, titulo, descripcion)
        showinfo("Actualizar Proyecto", "El proyecto ha sido actualizado correctamente.")
        el_tv.item(el_pry, values=(titulo, descripcion))
        scr.destroy()

def fn_scr_actualizar_proyecto(db_con, scr, el_pry_tv):
    scr_act_pryoyecto = Toplevel(scr)
    scr_act_pryoyecto.resizable(0, 0)
    scr_act_pryoyecto.title("Modificar Proyecto")
    scr_act_pryoyecto.geometry("400x250")
    scr_act_pryoyecto.grab_set()
    lbl_fuente = font.Font(weight="bold")

    el_pry = el_pry_tv.focus()
    el_pry_titulo = el_pry_tv.item(el_pry)["values"][0]
    el_pry_descripcion = el_pry_tv.item(el_pry)["values"][1]

    def fn_antes_cerrar():
        scr_act_pryoyecto.grab_set()
        scr_act_pryoyecto.destroy()

    scr_act_pryoyecto.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    var_titulo = StringVar()
    var_descripcion = StringVar()

    var_titulo.set(el_pry_titulo)
    var_descripcion.set(el_pry_descripcion)

    lbl_titulo = Label(scr_act_pryoyecto, text="Titulo:", font=lbl_fuente)
    lbl_descripcion = Label(scr_act_pryoyecto, text="Proyecto:", font=lbl_fuente)

    ipt_titulo = Entry(scr_act_pryoyecto, textvariable=var_titulo, width=25)
    ipt_descripcion = Entry(scr_act_pryoyecto, textvariable=var_descripcion, width=25)

    btn_pry_guardar = Button(
        scr_act_pryoyecto,
        text="Guardar",
        height=2,
        width=15,
        command=lambda: fn_scr_pry_guardar_proyecto(
            db_con,
            var_titulo.get(),
            var_descripcion.get(),
            el_pry_tv,
            scr_act_pryoyecto
        ),
    )

    btn_pry_cancelar = Button(scr_act_pryoyecto, text="Cancelar", height=2, width=15, command=fn_antes_cerrar)

    btn_pry_guardar.place(rely=0.5, anchor=CENTER)
    btn_pry_cancelar.place(rely=0.5, anchor=CENTER)
    separ1 = Separator(scr_act_pryoyecto, orient=HORIZONTAL)

    lbl_titulo.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    ipt_titulo.pack(side=TOP, expand=False, padx=5, pady=5)
    lbl_descripcion.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    ipt_descripcion.pack(side=TOP, expand=False, padx=5, pady=5)

    separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
    btn_pry_guardar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=6)
    btn_pry_cancelar.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

    scr.wait_window(scr_act_pryoyecto)

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# PANTALLA PRINCIPAL, MENU y TAB de pantalla
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def tv_proyecto_doble_click(event):
    global frm_proyecto

    item = tv_proyecto_grid.focus()

    if item is None or item == "":
        showerror("Actualizar Proyecto", "Para actualizar un proyecto debe seleccionar alguno de la grilla o hacer doble click sobre el mismo.")
        return

    fn_scr_actualizar_proyecto(db_con, frm_proyecto, tv_proyecto_grid)

def tv_archivo_doble_click(event):
    global frm_archivo

    item = tv_archivo_grid.focus()

    if item is None or item == "":
        showerror("Actualizar Archivo", "Para actualizar un archivo debe seleccionar alguno de la grilla o hacer doble click sobre el mismo.")
        return

    fn_scr_actualizar_archivo(db_con, frm_archivo, tv_archivo_grid)


def mostrar_frames():
    notebook.grid(row=1, column=0)

    frm_proyecto.grid(row=0, column=0)
    frm_archivo.grid(row=0, column=0)

    notebook.add(frm_proyecto, text="Proyectos")
    notebook.add(frm_archivo, text="Archivos")

    usuario_logueado = get_user()
    conectado = "Conectado: " + usuario_logueado["email"]

    lbl_str_conectado.set(conectado)
    lbl_conectado.grid(row=0, column=0, sticky=E)


def ocultar_frames():
    notebook.grid_forget()
    frm_proyecto.grid_forget()
    frm_archivo.grid_forget()
    lbl_conectado.grid_forget()

def fn_cambiar_usuario(nb, frm1, frm2):
    global filemenu

    if not askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
        return

    esta_logueado = get_user()

    if esta_logueado is None:
        return

    nb.grid_forget()
    frm1.grid_forget()
    frm2.grid_forget()
    filemenu.entryconfig("Modificar", state="disabled")
    filemenu.entryconfig("Cerrar Sesión", state="disabled")

    conectado = ""
    lbl_str_conectado.set(conectado)


def fn_usr_validar_login(db_con, scr_app):
    global filemenu
    fn_login(db_con, scr_app)
    esta_logueado = get_user()

    if esta_logueado is None:
        return

    mostrar_frames()
    filemenu.entryconfig("Modificar", state="normal")
    filemenu.entryconfig("Cerrar Sesión", state="normal")
    fn_cargar_proyectos(db_con, None)

def cargar_tv_archivos(pry_id):
    global db_con
    global tv_archivo_grid

    dict_archivos = archivo_seleccionar(db_con, pry_id, None)

    for item in tv_archivo_grid.get_children():
        tv_archivo_grid.delete(item)

    for key, valores in dict_archivos.items():
        tv_archivo_grid.insert("", index="end", text=key, values=(valores["nombre_archivo"], valores["ruta_archivo"]))

def frm_archivos_focus(event):
    global box
    global tv_archivo_grid
    global actual_proyecto
    usuario_logueado = get_user()

    actual_proyecto = box_value.get().split()

    dict_proyectos = proyecto_seleccionar(db_con, usuario_logueado["id"], None)

    if len(dict_proyectos) == 0:
        box_value.set("")
        box['values'] = None
        for item in tv_archivo_grid.get_children():
            tv_archivo_grid.delete(item)
    else:
        if len(dict_proyectos) != len(box['values']):
            opciones = list()

            for key, valores in dict_proyectos.items():
                opciones.append(str(key) + " - " + str(valores["nombre"]))

            box['values'] = opciones
            box.current(0)

        pry_id = box_value.get().split()[0]
        cargar_tv_archivos(pry_id)


def fn_combo_selected(event):
    global box
    global box_value

    pry_id = box_value.get().split()[0]
    dict_archivos = archivo_seleccionar(db_con, pry_id, None)

    for key, valores in dict_archivos.items():
        tv_archivo_grid.insert("", index="end", text=key, values=(valores["nombre_archivo"], valores["ruta_archivo"]))

def config(db_con, scr_app):
    global notebook
    global frm_proyecto
    global frm_archivo

    global tv_proyecto_grid
    global tv_archivo_grid
    global var_titulo
    global var_descripcion

    global var_nombre
    global ipt_nombre
    global var_ruta
    global box_value
    global box

    global lbl_conectado
    global lbl_str_conectado

    global filemenu

    menubar = Menu(scr_app)

    def fn_antes_cerrar():
        if askyesno("Salir", "¿Está seguro que desea salir de la aplicación?"):
            scr_app.grab_set()
            scr_app.destroy()

    scr_app.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Ingresar", command=lambda: fn_usr_validar_login(db_con, scr_app))
    filemenu.add_command(label="Registrar", command=lambda: fn_usr_registrar(db_con, scr_app))
    filemenu.add_command(label="Modificar", command=lambda: fn_scr_usr_modificar(db_con, scr_app))
    filemenu.add_command(label="Cerrar Sesión", command=lambda: fn_cambiar_usuario(notebook, frm_proyecto, frm_archivo))

    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=fn_antes_cerrar)

    menubar.add_cascade(label="Inicio", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Sobre...", command=lambda: fn_sobre(scr_app))
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    filemenu.entryconfig("Modificar", state="disabled")
    filemenu.entryconfig("Cerrar Sesión", state="disabled")

    scr_app.config(menu=menubar)

    lbl_str_conectado = StringVar()
    lbl_conectado = Label(scr_app, textvariable=lbl_str_conectado)
    lbl_conectado.grid(row=0, column=0, sticky=E)

    # -----------------------------------------------------------------------------------------------
    # TAB de PROYECTOS
    # -----------------------------------------------------------------------------------------------
    # Dividimos la pantalla de archivos en dos frames
    # La parte superior donde van los input
    # La parte inferior donde van la grilla y algunos botones
    # -----------------------------------------------------------------------------------------------

    frm_campos = Frame(frm_proyecto, width=600, height=150)
    frm_treeview = Frame(frm_proyecto, width=600, height=300)

    frm_campos.grid(row=1, column=0)
    separ1 = Separator(frm_proyecto, orient=HORIZONTAL)
    separ1.grid(row=2, columnspan=4, pady=5, sticky="ew")
    frm_treeview.grid(row=3, column=0)

    lbl_titulo = Label(frm_campos, text="Proyecto")
    lbl_titulo.grid(row=2, column=1, sticky=W)

    lbl_descripcion = Label(frm_campos, text="Descripción")
    lbl_descripcion.grid(row=3, column=1, sticky=W)

    # Definimos los input box y sus variables asociadas
    var_titulo = StringVar()
    ipt_titulo = Entry(frm_campos, textvariable=var_titulo, width=30)
    ipt_titulo.grid(row=2, column=2)

    var_descripcion = StringVar()
    ipt_descripcion = Entry(frm_campos, textvariable=var_descripcion, width=30)
    ipt_descripcion.grid(row=3, column=2)

    btn_guardar = Button(
        frm_campos,
        text="Guardar",
        command=lambda: fn_tv_guardar_proyecto(db_con, tv_proyecto_grid),
    )
    btn_guardar.grid(row=4, columnspan=3)

    tv_proyecto_grid = Treeview(frm_treeview)
    tv_proyecto_grid.grid(row=2, columnspan=3, sticky="nsew")
    tv_proyecto_grid.grid_columnconfigure(0, weight=1)
    tv_proyecto_grid["columns"] = ("one", 'two')
    tv_proyecto_grid.column("#0", width=50, minwidth=50, stretch=NO)
    tv_proyecto_grid.column("one", width=200, minwidth=200, stretch=NO)
    tv_proyecto_grid.column("two", width=250, minwidth=250, stretch=NO)

    tv_proyecto_grid.heading("#0", text="ID", anchor=W)
    tv_proyecto_grid.heading("one", text="Nombre", anchor=W)
    tv_proyecto_grid.heading("two", text="Descripción", anchor=W)

    tv_proyecto_grid.bind("<Double-1>", tv_proyecto_doble_click)

    btn_modificar = Button(
        frm_treeview,
        width=10,
        text="Modificar",
        command=lambda: tv_proyecto_doble_click(None),
    )
    btn_modificar.grid(row=1, column=0)

    btn_eliminar = Button(
        frm_treeview,
        width=10,
        text="Eliminar",
        command=lambda: fn_tv_borrar_proyecto(db_con, tv_proyecto_grid),
    )
    btn_eliminar.grid(row=1, column=2)

    # -----------------------------------------------------------------------------------------------
    # TAB de ARCHIVOS
    # -----------------------------------------------------------------------------------------------
    # Dividimos la pantalla de archivos en dos frames
    # La parte superior donde van los input
    # La parte inferior donde van la grilla y algunos botones
    # -----------------------------------------------------------------------------------------------

    lbl_combo = Label(frm_archivo, text="Proyectos:", font=lbl_fuente)
    lbl_combo.grid(row=2, column=0)

    box_value = StringVar()
    box = Combobox(frm_archivo, textvariable=box_value, state="readonly")
    box.grid(row=2, column=2)
    box.bind('<<ComboboxSelected>>', fn_combo_selected)

    lbl_nombre = Label(frm_archivo, text="Archivo")
    lbl_nombre.grid(row=3, column=1, sticky=W)

    lbl_descripcion = Label(frm_archivo, text="Ruta")
    lbl_descripcion.grid(row=4, column=1, sticky=W)

    # Definimos los input box y sus variables asociadas
    var_nombre = StringVar()
    ipt_nombre = Entry(frm_archivo, textvariable=var_nombre, width=30)
    ipt_nombre.grid(row=3, column=2)

    var_ruta = StringVar()
    ipt_ruta = Entry(frm_archivo, textvariable=var_ruta, width=30)
    ipt_ruta.grid(row=4, column=2)

    btn_guardar_archivo = Button(
        frm_archivo,
        text="Guardar",
        command=lambda: fn_tv_guardar_archivo(db_con, tv_archivo_grid),
    )

    btn_guardar_archivo.grid(row=5, column=0)

    btn_modificar_archivo = Button(
        frm_archivo,
        width=10,
        text="Modificar",
        command=lambda: tv_archivo_doble_click(None),
    )
    btn_modificar_archivo.grid(row=5, column=1)

    btn_eliminar_archivo = Button(
        frm_archivo,
        width=10,
        text="Eliminar",
        command=lambda: fn_tv_borrar_archivo(db_con, tv_archivo_grid),
    )
    btn_eliminar_archivo.grid(row=5, column=2)

    tv_archivo_grid = Treeview(frm_archivo)
    tv_archivo_grid.grid(row=6, columnspan=3, sticky="nsew")
    tv_archivo_grid.grid_columnconfigure(0, weight=1)
    tv_archivo_grid["columns"] = ("one", "two")
    tv_archivo_grid.column("#0", width=50, minwidth=50, stretch=NO)
    tv_archivo_grid.column("one", width=150, minwidth=150, stretch=NO)
    tv_archivo_grid.column("two", width=325, minwidth=325, stretch=NO)

    tv_archivo_grid.heading("#0", text="ID", anchor=W)
    tv_archivo_grid.heading("one", text="Nombre", anchor=W)
    tv_archivo_grid.heading("two", text="Ruta", anchor=W)

    vsb = Scrollbar(frm_archivo, orient="vertical", command=tv_archivo_grid.yview)
    vsb.grid(row=6, column=2, sticky='nse')
    tv_archivo_grid.configure(yscrollcommand=vsb.set)

    frm_archivo.bind("<FocusIn>", frm_archivos_focus)

    tv_archivo_grid.bind("<Double-1>", tv_archivo_doble_click)


if __name__ == "__main__":
    db_con = db.conectar()
    db_con.row_factory = sqlite3.Row

    cursor = db_con.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')

    try:
        os.remove("temp")
    except (OSError, IOError) as err:
        print("Error: unable to write file (", err, ")")

    app_start(db_con)
