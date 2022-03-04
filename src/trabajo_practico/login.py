from tkinter.ttk import Separator
from database import login, registrar
from tkinter import (
    BOTH,
    CENTER,
    HORIZONTAL,
    LEFT,
    RIGHT,
    TOP,
    Button,
    Entry,
    Label,
    StringVar,
    Tk,
    font,
    X,
)


def main():
    scr_login = Tk()
    scr_login.geometry("400x250")
    scr_login.title("TransferX")

    usuario = StringVar()
    clave = StringVar()

    Label(
        scr_login, text="Ingrese tus credenciales para comenzar", font=("Calibri", 13)
    ).pack()
    Label(scr_login, text="")

    lbl_fuente = font.Font(weight="bold")

    lbl_user = Label(scr_login, text="Usuario:", font=lbl_fuente)
    lbl_pass = Label(scr_login, text="Contraseña:", font=lbl_fuente)

    input_user = Entry(scr_login, textvariable=usuario, width=25)
    input_pass = Entry(scr_login, textvariable=clave, width=25, show="*")

    # Button(scr_login, text="Ingresar", height=2, width=15, command=login).pack(side=LEFT)
    btn_login = Button(scr_login, text="Ingresar", height=2, width=15, command=login)
    btn_reg = Button(scr_login, text="Registrar", height=2, width=15, command=registrar)

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

    scr_login.mainloop()


main()
