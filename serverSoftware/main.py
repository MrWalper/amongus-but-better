import socket
import misc
from ursina import *
import packetTranslator
import packets
import simulation

config = misc.openJson("serverSoftware\systemFiles\config.json")
reciver = packetTranslator.reciver()

simulation = Ursina()

ground = Entity(
    model = "cube",
    texture = "grass",
    collider = "box",
    scale = 10
)

entityList = []

class server():
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 5005

        sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        sock.bind((self.ip,self.port))
        print("Server online")

        while True:
            returnPacket = "ok"
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if config["logPackets"]:
                print("received message: %s" % data)
            latestPacket = reciver.recive(data)

            if type(latestPacket) == packets.entityMove: 
                entityList[latestPacket.packetId].position = latestPacket
            elif type(latestPacket) == packets.playerJoin:
                entityList.append(simulation.newEntity)
                latestPacket = []
                entityList[-1].isPlayer = True
            if type(latestPacket) == packets.requestSync():
                returnPacket = f"3:[{latestPacket.rPlayerPos[0]},{latestPacket.rPlayerPos[1]},{latestPacket.rPlayerPos[2]}]:{latestPacket.rPlayerAction}:{latestPacket.rMisc}"
            
            sock.sendto(str.encode(latestPacket),addr)
                
            simulation.step()

