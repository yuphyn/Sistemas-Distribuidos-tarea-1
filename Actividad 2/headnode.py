import socket
import threading
import time

class T1 (threading.Thread):
    def __init__(self):
        super(T1 , self).__init__(name="T1 thread")
        print ('I am T1')

    def run(self):
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
        # regarding socket.IP_MULTICAST_TTL
        # ---------------------------------
        # for all packets sent, after two hops on the network the packet will not 
        # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
        MULTICAST_TTL = 2

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        sock.sendto("robot".encode(), (MCAST_GRP, MCAST_PORT))
        
        while True:
            consulta = "estan operativos?"
            sent = sock.sendto(consulta.encode('ascii'), (MCAST_GRP,MCAST_PORT))
            data1, server1 = sock.recvfrom(1024)
            print(server1,' está: ',data1)
            time.sleep(5)

class T2 (threading.Thread):
    def __init__(self):
        super(T2 , self).__init__(name="T2 thread")
        print ('I am T2')

    def run(self):
        'hola'

t1 = T1()
t2 = T2()

t1.start()
t2.start()