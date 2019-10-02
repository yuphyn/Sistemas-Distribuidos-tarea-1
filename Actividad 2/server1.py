import socket
import struct
import threading


class T1 (threading.Thread):
    def __init__(self):
        super(T1 , self).__init__(name="T1 thread")
        print ('I am T1')

    def run(self):
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
        IS_ALL_GROUPS = True

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if IS_ALL_GROUPS:
            # on this port, receives ALL multicast groups
            sock.bind(('', MCAST_PORT))
        else:
            # on this port, listen ONLY to MCAST_GRP
            sock.bind((MCAST_GRP, MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        while True:
            data, address = sock.recvfrom(1024)
            respuesta = "sep"
            sock.sendto(respuesta.encode('ascii'), address)

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