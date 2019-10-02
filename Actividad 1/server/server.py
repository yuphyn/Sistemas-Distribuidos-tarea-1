import socket

def Main():
    host = "127.0.0.1"
    port = 5000 #Puerto
    file = open("log.txt", "w")
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(5) #CAntidad de connecciones permitidas
    print("Esperando conección")
    conn, addr = mySocket.accept()
    file.write("Se conecto a: " + str(addr)+"\n")
    file.close()
    print("Conectado al cliente")
    while True:
        data = conn.recv(1024).decode()
        file = open("log.txt", "a")
        file.write("mensaje del cliente: "+" "+str(data)+"\n")
        file.close()
        conn.send(data.encode())
        conn.close()
        data= "mensaje del cliente: "+str(data)
        print("Conección cerrada")
        print("Esperando cliente")
        conn, addr = mySocket.accept()
        file = open("log.txt", "a")
        file.write("Se conectó a: " + str(addr)+"\n")
        file.close()

if __name__ == '__main__':
    Main()
