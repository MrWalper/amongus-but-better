from ursina import *
import time

class chainEntity(Entity):
    def __init__(self):
        super().__init__(model="assets/3d-models/chain_entity.obj",
                         texture="assets/texture/chain_entity.png",
                        collider = "box",
                        visible=True)
    
def shootOut(angle,startPoint:Vec3,ignoreEntity:list):
    chainSound = Audio("assets\sound\metal-chain-uncut.mp3",autoplay=True)
    chain = chainEntity()
    ignoreEntity.append(chain)
    hitInfo = raycast(startPoint,angle,100,ignore=[chain])
    chain.position = startPoint
    chain.world_rotation = angle
    if hitInfo.hit:
        goal = hitInfo.entity.model
        print(goal)


