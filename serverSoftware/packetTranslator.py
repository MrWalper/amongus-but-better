from ursina import *
import scriptsToImport.misc as misc
import scriptsToImport.networking.packets as packets

class reciver():
    def __init__(self):
        print("Reciver online")
    
    def recive(self,packet:bytes):
        self.packet = packet
        self.packet = self.packet.decode("utf-8")
        self.packet.split(":")

        if self.packet[0] == "0":
            return packets.keepAlivePacket()
        
        elif self.packet[0] == "1":
            return packets.entityMove(start=self.packet[1],goal=self.packet[2],entityId=self.packet[3])
        
        elif self.packet[0] == "2":
            return packets.playerKeyPress(key=self.packet[1])
        
        elif self.packet[0] == "3":
            self.rPlayerPos = packet[1] == 0
            self.rPlayerAction = packet[2] == 0
            self.rMisc = packet[3] == 0

            return packets.requestSync(rPlayerPos=self.rPlayerPos,rPlayerAction=self.rPlayerAction,rMisc=self.rMisc,)

        elif self.packet[0] == "4":
            self.playerName = packet[1]

            return packets.playerJoin(playerName=self.playerName)
