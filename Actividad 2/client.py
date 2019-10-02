import socket

def Main():
    host = '127.0.0.1'
    port = 5000
    mySocket = socket.socket()
    mySocket.connect((host,port))

    message = "soy el cliente"
    mySocket.send(message.encode())
    data = mySocket.recv(1024).decode()
    print(data)
    file = open("registro_cliente.txt", "w")
    file.write("El servidor guardo el mensaje en el nodo: "+data+"\n")
    file.close()
    mySocket.close()

if __name__ == '__main__':
    Main()
