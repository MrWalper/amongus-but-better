import socket
"""
When sending packets, send them in this format:
packetId:data1:data2 etc.
the order of the data will be determined by order that it does by in packet.py
If there is no data to send (for example in keepAlivePacket)
then add 0 after packetId
"""
class networking():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

        def sendPacket(self,data,packetType):
            packet = data + ":" + packetType
            self.sock.sendto(bytes(packet, "utf-8"), (self.ip, self.port))
