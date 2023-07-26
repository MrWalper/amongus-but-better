import socket

class networking():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

        def sendPacket(self,data,packetType):
            packet = data + ":" + packetType
            self.sock.sendto(bytes(packet, "utf-8"), (self.ip, self.port))
