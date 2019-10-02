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
    file.close()
    print("Conectado al cliente")
    print("Peticion salir -> cerrar coneccion")
    while True:
            data = conn.recv(1024).decode()
            file = open("log.txt", "a")
            file.write("peticion"+" "+str(data)+"\n")
            file.close()
            if(data=="salir"):
                print("se cerró la conección con el cliente")
                print("------------------------------------")
                conn.close()
                print("Esperando coneccion")
                conn, addr = mySocket.accept()
                print("Conectado al cliente")
                print("Peticion salir -> cerrar coneccion")
                file = open("log.txt", "a")
                file.write("Se conecto " + str(addr)+"\n")
                file.close()
                continue
            data= "Se realizo la peticion"+" " +str(data)
            conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    Main()
