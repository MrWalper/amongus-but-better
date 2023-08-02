import socket
from scriptsToImport.misc import openJson

"""
When sending packets, send them in this format:
packetId:data1:data2 etc.
The order of the data will be determined by order that it does by in packet.py
If there is no data to send (for example in keepAlivePacket)
then add 0 after packetId

If you want to send coords do it like this:
[x,y,z]
"""

config = openJson("system-files\config.json")["logpackets"]

class networking():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

    def sendPacket(self,data:str,packetType:int):
        self.packet = str(packetType) + ":" + data
        self.sock.sendto(bytes(self.packet, "utf-8"), (self.ip, self.port))
        if config:
            print(f"Packet sent {self.packet}")

    def listen(self):
        self.packetGot = self.sock.recvfrom(1024)
        return self.packetGot