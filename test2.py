import scriptsToImport.networking.send as send

sender = send.networking(ip="127.0.0.1",port=5005)
sender.sendPacket(data="Walper",packetType=0)