"""
Escriba un programa que guarde en una variable una contraseña y
consulte al usuario por la contraseña hasta que esta sea correcta.
El programa debe informar al usuario si la contraseña fue correcta o no.
"""

contrasenia = "Learning"
intentos = 5


while intentos > 0:
    adivina = input("Intente adivinar la contraseña, ingrese una: ")
    if contrasenia == adivina:
        print("Has adivinado!!!")
        break

    intentos -= 1
    print(f"No adivinaste, te quedan {intentos} intentos.")
