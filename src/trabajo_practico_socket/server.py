import socket
import select

LEN_PREFIJO = 10

IP = "localhost"
PORT = 80

# socket.AF_INET - IPv4
# socket.SOCK_STREAM - TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

# Lista de sockets a trabajar
sockets_list = [server_socket]

# Lista de clientes conectados
clients = {}

def mensaje_entrante(client_socket):
    try:
        prefijo_mensaje = client_socket.recv(LEN_PREFIJO)

        if not len(prefijo_mensaje):
            return False

        longitud_mensaje = int(prefijo_mensaje.decode('utf-8').strip())
        return {'prefijo': prefijo_mensaje, 'informacion': client_socket.recv(longitud_mensaje)}

    except Exception as e:
        # Si el servidor cierra la conexion o recibimos un mensaje vacio
        return False

print(f'Sala de chat escuchando en {IP}:{PORT}...')

while True:

    # https://docs.python.org/3/library/select.html
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for socket_activo in read_sockets:

        # Si se trata del mismo server, es una conexion entrante (nueva)
        if socket_activo == server_socket:

            client_socket, client_address = server_socket.accept()
            usuario_entrante = mensaje_entrante(client_socket)

            if usuario_entrante is False:
                continue

            sockets_list.append(client_socket)

            # Agregamos informacion del cliente conectado
            clients[client_socket] = usuario_entrante

            print(f"Nuevo cliente {client_address[0]}:{client_address[1]}, usuario: {usuario_entrante['informacion'].decode('utf-8')}")

        # Se trata de un envio de mensaje de un cliente ya agregado
        else:

            message = mensaje_entrante(socket_activo)

            if message is False:
                print(f"Se cerró la conexion: {clients[socket_activo]['informacion'].decode('utf-8')}")
                sockets_list.remove(socket_activo)
                del clients[socket_activo]
                continue

            usuario_entrante = clients[socket_activo]

            print(f'Mensaje recibido desde {usuario_entrante["informacion"].decode("utf-8")}: {message["informacion"].decode("utf-8")}')

            # Ahora vamos a enviar los mensajes al resto de usuarios
            for client_socket in clients:
                # Que no sea el mismo usuario
                if client_socket != socket_activo:
                    client_socket.send(usuario_entrante['prefijo'] + usuario_entrante['informacion'] + message['prefijo'] + message['informacion'])

    for socket_activo in exception_sockets:
        sockets_list.remove(socket_activo)
        del clients[socket_activo]
