from ursina import *
import scriptsToImport.misc as misc
import time
import random

class Enemy(Entity):
    def __init__(self,listToIgnore:list,target:Entity):
        self.listToIgnore = listToIgnore
        self.target = target

        super().__init__(
            model="cube",
            color=color.red,
            Collider="box"
        )
        self.originVar = self.world_position + (self.up*.5)
        self.didIAttack = False
        self.lastActivated = 0
        self.attackCounter = 0
        self.moveCounter = 0

    def update(self):
        if self.attackCounter == 10:
            if self.world_position - self.target.position <= 3 and self.world_position - self.target.position >= -3:
                if not self.didIAttack:
                    self.attack = raycast(origin=self.originVar,direction=self.world_rotation,ignore=self.listToIgnore,distance=2)
                    if self.attack.entity.isPlayer:
                        self.attack.entity.healthBar.value -= 5
                    self.lastActivated = int(time.time())
                    self.didIAttack = True
                else: 
                    if misc.cooldown(lastActivated=self.lastActivated,cooldown=0.5):
                        self.attack = raycast(origin=self.originVar,direction=self.world_rotation,ignore=self.listToIgnore,distance=2)
                        if self.attack.entity.isPlayer:
                            self.attack.entity.healthBar.value -= 5
                        self.lastActivated = int(time.time())
            self.attackCounter = 0
        else:
            self.attackCounter += 1
        
        if self.moveCounter == 3:
            if not self.target.world_position == self.world_position + self.forward:
                self.look_at(target=self.target)
                if random.randint(0,10) == 3:
                    self.world_position += self.forward
            self.moveCounter = 0
        else:
            self.moveCounter += 1
        