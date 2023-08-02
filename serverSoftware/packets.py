class keepAlivePacket():
    def __init__(self):
        self.id = 0
        
class entityMove():
    def __init__(self,start:int,goal:int,entityId:int):
        self.start = start
        self.goal = goal
        self.entityID = entityId
        self.id = 1

class playerKeyPress():
    def __init__(self,key:int):
        self.key = key
        self.id = 2

class requestSync():
    def __init__(self,rPlayerPos:bool,rPlayerAction:bool,rMisc:bool):
        self.rPlayerPos = rPlayerPos
        self.rPlayerAction = rPlayerAction
        self.rMisc = rMisc
        self.id = 3

class playerJoin():
    def __init__(self,playerName:str):
        self.playerName = playerName
        self.id = 4
