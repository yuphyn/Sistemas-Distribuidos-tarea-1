import socket

def Main():
    host = "127.0.0.1"
    port = 5000 #Puerto
    file = open("log.txt", "w")
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(5) #CAntidad de connecciones permitidas
    print("Esperando coneccion")
    conn, addr = mySocket.accept()
    file.write("Se conecto " + str(addr)+"\n")
    print("Peticion salir -> cerrar coneccion")
    while True:
            data = conn.recv(1024).decode()
            file.write("peticion"+" "+str(data)+"\n")
            if(data=="salir"):
                break
            data= "Se realizo la peticion"+" " +str(data)
            conn.send(data.encode())

    file.close()
    conn.close()

if __name__ == '__main__':
    Main()
