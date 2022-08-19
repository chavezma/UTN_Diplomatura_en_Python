import socket
import select
import errno
import sys

LEN_PREFIJO = 10

IP = "localhost"
PORT = 80

# Pedimos el nombre del usuario
get_usuario = input("Usuario: ")
print("Cada tanto presionar ENTER para liberar la pantalla e imprimir los mensajes entrantes (si los hubiera)")

# socket.AF_INET - IPv4
# socket.SOCK_STREAM - TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)
usuario_local = get_usuario.encode('utf-8')
usuario_local_header = f"{len(usuario_local):<{LEN_PREFIJO}}".encode('utf-8')
client_socket.send(usuario_local_header + usuario_local)

while True:

    # Se bloquea la terminal esperando un mensaje
    mensaje_escrito = input(f'{get_usuario} > ')

    # Si se ingresa un mensaje se envia
    if mensaje_escrito:
        mensaje_escrito = mensaje_escrito.encode('utf-8')
        mensaje_prefijo = f"{len(mensaje_escrito):<{LEN_PREFIJO}}".encode('utf-8')
        client_socket.send(mensaje_prefijo + mensaje_escrito)

    # Aprovechamos que se libera el input para ver si hay mensajes desde los demás usuarios
    try:
        while True:
            usuario_local_header = client_socket.recv(LEN_PREFIJO)

            if not len(usuario_local_header):
                print('Connection closed by the server')
                sys.exit()

            # Parseamos el usuario y mensaje
            usuario_len_prefijo = int(usuario_local_header.decode('utf-8').strip())
            usuario_local = client_socket.recv(usuario_len_prefijo).decode('utf-8')
            mensaje_prefijo = client_socket.recv(LEN_PREFIJO)
            mensaje_escrito_len = int(mensaje_prefijo.decode('utf-8').strip())
            mensaje_escrito = client_socket.recv(mensaje_escrito_len).decode('utf-8')
            print(f'{usuario_local} > {mensaje_escrito}')

    except IOError as e:
        # errores contemplados para la recepcion del mensaje
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print(f'Ocurrió un error: {str(e)}')
            sys.exit()

        # Si son esos continuamos
        continue

    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')
        sys.exit()
