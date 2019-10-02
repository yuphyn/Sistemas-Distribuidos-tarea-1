import socket

def Main():
        host = '127.0.0.1'
        port = 5000
        file = open("respuesta.txt", "w")
        file.close()
        mySocket = socket.socket()
        mySocket.connect((host,port))

        while True:
            message = input("Introduce instruccion: ")
            mySocket.send(message.encode())
            data = mySocket.recv(1024).decode()
            if (data != ""):
                file = open("respuesta.txt", "a")
                file.write(data+"\n")
                file.close()
            if(message=="salir"):
                file = open("respuesta.txt", "a")
                file.write("Se realizo la peticion salir")
                file.close()
                break
        mySocket.close()

if __name__ == '__main__':
    Main()
