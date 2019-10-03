import socket
import threading
import time
import datetime
import random

puertos=[]
class T1 (threading.Thread):
    def __init__(self):
        super(T1 , self).__init__(name="T1 thread")
        print ('I am T1')

    def run(self):
        file = open("hearbeat_server.txt", "w")
        file.close()
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
        global puertos
        # regarding socket.IP_MULTICAST_TTL
        # ---------------------------------
        # for all packets sent, after two hops on the network the packet will not 
        # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
        MULTICAST_TTL = 2

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        sock.settimeout(1)
        
        while True:
            consulta = "estan operativos?"
            sent = sock.sendto(consulta.encode('ascii'), (MCAST_GRP,MCAST_PORT))
            
            time.sleep(5)
            puertos=[]

            while True:
                try:
                    data1, server1 = sock.recvfrom(1024)
                    ts = time.time()
                    data1=data1.decode()
                    if data1== "datanode 1: active":
                        puertos.append(['127.1.1.1',4000])
                    if data1== "datanode 2: active":
                        puertos.append(['127.1.1.2',4500])
                    if data1== "datanode 3: active":
                        puertos.append(['127.1.1.3',4700])
                    hora = datetime.datetime.fromtimestamp(ts).strftime("%d/%m/%Y - %H:%M:%S --- ")
                    save = hora+data1+"\n"
                    file = open("hearbeat_server.txt", "a")
                    file.write(save)
                    file.close()
                    print("los puertos"+ str(puertos))
                except (socket.timeout):
                    break

                

class T2 (threading.Thread):
    def __init__(self):
        super(T2 , self).__init__(name="T2 thread")
        print ('I am T2')

    def run(self):
        host = "127.0.0.1"
        port = 5000 #Puerto
        global puertos
        mySocket = socket.socket()
        mySocket.bind((host,port))
        mySocket.listen(5) #CAntidad de connecciones permitidas
        print("Esperando conexión")
        print (puertos)
        conn, addr = mySocket.accept()
        print("Conectado al cliente")
        file = open("registro_server.txt", "w")
        file.close()
        while True:
            data = conn.recv(1024).decode()

            ####Envio a nodo
            var=random.choice(puertos)
            port2 = var[1]
            host2 = var[0]
            mySocket2 = socket.socket()
            mySocket2.connect((host2,port2))
            mySocket2.send(data.encode())

            respuesta = mySocket2.recv(1024).decode()
            mySocket2.close()

            file = open("registro_server.txt", "a")
            file.write("Guardado en el "+respuesta+"\n")
            file.close()

            ######
            send_to_client = "Guardado exitoso en el "+respuesta
            conn.send(send_to_client.encode())
            conn.close()
            print("Conección cerrada")
            print("Esperando cliente")
            conn, addr = mySocket.accept()

t1 = T1()
t2 = T2()

t1.start()
t2.start()