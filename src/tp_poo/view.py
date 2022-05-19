# from tkinter import *
# from tkinter.messagebox import *
# from tkinter import ttk, Tk, Label, Button, StringVar, DoubleVar, Entry

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, askyesno
import tkinter.font as tkFont

# ##############################################
# VISTA
# ##############################################
class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("Esto no es una copia")
        self.titulo = tk.Label(self, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=tk.W + tk.E)

        self.producto = ttk.Label(self, text="Producto")
        self.producto.grid(row=1, column=1, sticky=tk.W)
        self.cantidad = ttk.Label(self, text="Cantidad")
        self.cantidad.grid(row=2, column=1, sticky=tk.W)
        self.precio = ttk.Label(self, text="Precio")
        self.precio.grid(row=3, column=1, sticky=tk.W)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val, self.c_val = tk.StringVar(), tk.DoubleVar(), tk.DoubleVar()
        w_ancho = 20

        self.entrada1 = ttk.Entry(self, textvariable=self.a_val, width=w_ancho)
        self.entrada1.grid(row=1, column=2)
        self.entrada2 = ttk.Entry(self, textvariable=self.b_val, width=w_ancho)
        self.entrada2.grid(row=2, column=2)
        self.entrada3 = ttk.Entry(self, textvariable=self.c_val, width=w_ancho)
        self.entrada3.grid(row=3, column=2)

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor=tk.W)
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="cantidad")
        self.tree.heading("col3", text="precio")
        self.tree.grid(row=10, column=0, columnspan=4)

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.grid(row=10, column=4, sticky='nse')
        self.tree.configure(yscrollcommand=vsb.set)

        self.boton_alta = ttk.Button(self, text="Alta", command=self.alta)
        self.boton_alta.grid(row=6, column=0)

        self.boton_actualizar = ttk.Button(self, text="Actualizar", command=self.actualizar)
        self.boton_actualizar.grid(row=6, column=1)

        self.boton_borrar = ttk.Button(self, text="Borrar", command=self.borrar)
        self.boton_borrar.grid(row=6, column=2)

        self.boton_consultar = ttk.Button(self, text="Consultar", command=self.reiniciar_treeview)
        self.boton_consultar.grid(row=6, column=3)

    def reiniciar_treeview(self,):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        resultado = self.controller.getProductos()

        for fila in resultado:
            print(fila)
            self.tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

    def alta(self, ):
        print("Alta de Producto estamos.")
        producto = self.a_val.get()
        cantidad = self.b_val.get()
        precio = self.c_val.get()

        if not self.controller.alta(producto, cantidad, precio):
            showerror("Alta de Producto", "Error al guardar producto...")
            return

        showinfo("Alta de Producto", "El producto ha sido dado de alta exitosamente.")

        self.a_val.set("")
        self.b_val.set("")
        self.c_val.set("")
        self.reiniciar_treeview()

    def borrar(self,):
        item = self.tree.focus()

        if item is None or item == "":
            showerror("Borrar Producto", "Para borrar un producto debe seleccionarlo previamente.")
            return

        prod_id = self.tree.item(item)["text"]

        print("prod_id: ", prod_id)

        if askyesno("Borrar Producto", "¿Está seguro que desea borrar el producto?"):
            self.controller.borrar(prod_id)
            showinfo("Borrar Archivo", "El producto fue borrado correctamente.")
            self.tree.delete(item)

    def actualizar(self,):
        item = self.tree.focus()

        if item is None or item == "":
            showerror("Actualizar Producto", "Para actualizar un producto debe seleccionarlo previamente.")
            return

        options_popup = ActualizarProducto(self)
        options_popup.wait_window()

    def main(self):
        self.mainloop()


class ActualizarProducto(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master

        self.resizable(0, 0)
        self.title("Modificar Producto")
        self.geometry("400x250")
        self.grab_set()
        self.lbl_fuente = tkFont.Font(weight="bold")

        prod = master.tree.focus()
        prod_nombre = master.tree.item(prod)["values"][0]
        prod_cantidad = master.tree.item(prod)["values"][1]
        prod_precio = master.tree.item(prod)["values"][2]

        self.protocol("WM_DELETE_WINDOW", self.fn_antes_cerrar)

        self.var_nombre = tk.StringVar()
        self.var_cantidad = tk.DoubleVar()
        self.var_precio = tk.DoubleVar()

        self.var_nombre.set(prod_nombre)
        self.var_cantidad.set(prod_cantidad)
        self.var_precio.set(prod_precio)

        self.lbl_nombre = tk.Label(self, text="Nombre:", font=self.lbl_fuente)
        self.lbl_cantidad = tk.Label(self, text="Cantidad:", font=self.lbl_fuente)
        self.lbl_precio = tk.Label(self, text="Precio:", font=self.lbl_fuente)

        self.ipt_nombre = tk.Entry(self, textvariable=self.var_nombre, width=25)
        self.ipt_cantidad = tk.Entry(self, textvariable=self.var_cantidad, width=25)
        self.ipt_precio = tk.Entry(self, textvariable=self.var_precio, width=25)

        self.btn_guardar = tk.Button(
            self,
            text="Guardar",
            height=2,
            width=15,
            command=self.actualizar_producto,
        )

        self.btn_cancelar = tk.Button(self, text="Cancelar", height=2, width=15, command=self.fn_antes_cerrar)

        self.btn_guardar.place(rely=0.5, anchor=tk.CENTER)
        self.btn_cancelar.place(rely=0.5, anchor=tk.CENTER)
        self.separ1 = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.lbl_nombre.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.ipt_nombre.pack(side=tk.TOP, expand=False, padx=5, pady=5)
        self.lbl_cantidad.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.ipt_cantidad.pack(side=tk.TOP, expand=False, padx=5, pady=5)
        self.lbl_precio.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.ipt_precio.pack(side=tk.TOP, expand=False, padx=5, pady=5)

        self.separ1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.btn_guardar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=6)
        self.btn_cancelar.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # self.wait_window(master)
    def fn_antes_cerrar(self,):
        self.grab_set()
        self.destroy()

    def actualizar_producto(self,):
        print("actualizar_producto: ")
        el_prod = self.master.tree.focus()
        print("actualizar_producto el_prod: ", el_prod)

        if askyesno("Actualizar Proyecto", "¿Está seguro que desea actualizar el producto seleccionado?"):
            prod_id = self.master.tree.item(el_prod)["text"]
            self.master.controller.actualizar(prod_id, self.var_nombre.get(), self.var_cantidad.get(), self.var_precio.get())
            showinfo("Actualizar Proyecto", "El proyecto ha sido actualizado correctamente.")
            self.master.tree.item(el_prod, values=(self.var_nombre.get(), self.var_cantidad.get(), self.var_precio.get()))
            self.destroy()

