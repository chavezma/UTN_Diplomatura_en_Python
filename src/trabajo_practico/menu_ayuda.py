from tkinter import BOTH, CENTER, LEFT, Button, Label, Toplevel, font

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# Sobre
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------


def fn_sobre(scr_app):
    scr_sobre = Toplevel(scr_app)
    scr_sobre.geometry("400x160")
    scr_sobre.title("TransferX - Sobre")
    scr_sobre.grab_set()
    lbl_fuente = font.Font(weight="bold")

    speech = """
    Esta aplicación ha sido desarrollada por el alumno Matias Chavez.
    Para la Diplomatura en Python
    Etapa: Nivel Inicial
    Fecha: Abril 2022
    """

    def fn_antes_cerrar():
        scr_sobre.grab_set()
        scr_sobre.destroy()

    scr_sobre.protocol("WM_DELETE_WINDOW", fn_antes_cerrar)

    lbl_titulo = Label(
        scr_sobre, text="Información sobre la aplicación", font=("Calibri", 13)
    )
    lbl_desc = Label(scr_sobre, text=speech)

    btn_volver = Button(
        scr_sobre,
        text="Volver",
        height=1,
        width=15,
        command=lambda: fn_antes_cerrar(),
    )

    lbl_titulo.grid(row=1, column=1)
    lbl_desc.grid(row=2, column=0, columnspan=3)
    btn_volver.grid(row=3, column=1)

    # Indicamos que la ventana principal espere por la finalizacion del login.
    scr_app.wait_window(scr_sobre)
