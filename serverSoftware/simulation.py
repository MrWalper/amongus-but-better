from ursina import *

class newEntity(Entity):
    def __init__(self,):
        super().__init__(
            model="capsule",
            collider="box",
            entityId=0
        )
        self.isPlayer = False

