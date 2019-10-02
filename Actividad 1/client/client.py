import socket

def Main():
    host = '127.0.0.1'
    port = 5000
    file = open("respuesta.txt", "w")
    file.close()
    mySocket = socket.socket()
    mySocket.connect((host,port))

    message = "Hola, soy el cliente"
    mySocket.send(message.encode())
    data = mySocket.recv(1024).decode()
    file = open("respuesta.txt", "a")
    file.write("El servidor guardo el mensaje: "+data+"\n")
    file.close()
    mySocket.close()

if __name__ == '__main__':
    Main()