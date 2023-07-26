from ursina import *
import scriptsToImport.misc as misc
import time
import random

class Enemy(Entity):
    def __init__(self,listToIgnore:list,target:Entity,ground:Entity):
        self.ground = ground
        self.listToIgnore = listToIgnore
        self.target = target

        super().__init__(
            model="wireframe_cube",
            color=color.red,
            collider="box",
            scale=2
        )

        self.originVar = self.world_position + (self.up*.5)
        self.didIAttack = False
        self.lastActivated = 0
        self.attackCounter = 0
        self.moveCounter = 0

    def update(self):
        if self.attackCounter == 10:
            if not self.didIAttack:
                if self.intersects(self.target.controller).hit:
                    self.target.healthBar.value -= 5
                    self.color = color.green
                    print("Hit")
                else:
                    self.color = color.red
                self.lastActivated = int(time.time())
                self.didIAttack = True
            else: 
                if self.intersects(self.target.controller).hit:
                    self.target.healthBar.value -= 5
                    self.color = color.green
                    print("Hit")
                else:
                    self.color = color.red
                self.lastActivated = int(time.time())
            self.attackCounter = 0
        else:
            self.attackCounter += 1

        if self.moveCounter == 5:
            self.look_at(target=self.target)
            if random.randint(0,10) == 3:
                self.world_position += self.forward
            self.moveCounter = 0
        else:
            self.moveCounter += 1
