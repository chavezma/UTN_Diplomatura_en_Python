import tkinter
from tkinter import colorchooser

app = tkinter.Tk()
app.title("GUI Application of Python")

titulo = tkinter.Label(app, text="Ejercicio Desafio", height=1, width=60)
titulo.grid(
    row=0, column=0, columnspan=4, padx=1, pady=1, sticky=(tkinter.W + tkinter.S)
)

# Definimos los labels

lbl_titulo = tkinter.Label(app, text="Título")
lbl_titulo.grid(row=1, column=0, sticky=tkinter.W)

lbl_ruta = tkinter.Label(app, text="Ruta")
lbl_ruta.grid(row=2, column=0, sticky=tkinter.W)

lbl_descripcion = tkinter.Label(app, text="Descripcion")
lbl_descripcion.grid(row=3, column=0, sticky=tkinter.W)

# Definimos los input box y sus variables asociadas
var_titulo = tkinter.StringVar()
ipt_titulo = tkinter.Entry(app, textvariable=var_titulo, width=30)
ipt_titulo.grid(row=1, column=1)

var_ruta = tkinter.StringVar()
ipt_ruta = tkinter.Entry(app, textvariable=var_ruta, width=30)
ipt_ruta.grid(row=2, column=1)

var_descripcion = tkinter.StringVar()
ipt_descripcion = tkinter.Entry(app, textvariable=var_descripcion, width=30)
ipt_descripcion.grid(row=3, column=1)


def fn_imprimir_valores():
    print(f"{var_titulo.get()} - {var_ruta.get()} - {var_descripcion.get()}")
    print("")


def fn_cambiar_color():
    color = colorchooser.askcolor(title="Choose color")
    app.configure(background=color[1])


btn_aceptar = tkinter.Button(app, text="Imprimir", command=fn_imprimir_valores)
btn_aceptar.grid(row=4, column=0)

btn_cambiar_color = tkinter.Button(app, text="Cambiar Color", command=fn_cambiar_color)
btn_cambiar_color.grid(row=4, column=2)

app.mainloop()
