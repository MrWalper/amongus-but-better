from ursina import *
import time

class chainEntity(Entity):
    def __init__(self):
        super().__init__(model="assets/3d-models/chain_entity.obj",
                         texture="assets/texture/chain_entity.png",
                        collider = "box",
                        visible=True)
        self.isPlayer = False
    
def shootOut(angle,startPoint:Vec3,ignoreEntity:list):
    chainSound = Audio("assets\sound\metal-chain-uncut.mp3",autoplay=True)
    hitInfo = raycast(startPoint,angle,100)
    return(hitInfo)
