import socket

def Main():
        host = '127.0.0.1'
        port = 5000
        file = open("respuesta.txt", "w")
        mySocket = socket.socket()
        mySocket.connect((host,port))

        while True:
            message = raw_input("Introduce instruccion: ")

            mySocket.send(message.encode())
            data = mySocket.recv(1024).decode()
            file.write(data+"\n")
            if(message=="salir"):
                break
        file.write("Se realizo la peticion salir")
        file.close()
        mySocket.close()

if __name__ == '__main__':
    Main()
