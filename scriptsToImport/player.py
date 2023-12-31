from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
import scriptsToImport.misc as misc
from ursina.prefabs.health_bar import HealthBar

class Player(Entity):
    def __init__(self,**kwargs):
        self.controller = FirstPersonController(**kwargs,collider="box")

        super().__init__(parent=self.controller,
                         scale = 3,
                         model="assets/3d-models/player_basic.obj",
                         texture="assets/texture/player_red.png",
                         )

        self.cube = Entity(parent=self.controller.camera_pivot,
                            position=Vec3(0.7,-1,1.5),
                            rotation=Vec3(0,170,0),
                            model="cube",
                            texture="grass",
                            visible=False)
        
        self.chainItem = Entity(parent=self.controller.camera_pivot,
                            position=Vec3(0.7,-1,1.5),
                            rotation=Vec3(0,170,0),
                            model="assets/3d-models/item_chain_model.obj",
                            texture="assets/texture/item_chain_texture.png",
                            visible=False)
        
        self.stabby = Entity(parent=self.controller.camera_pivot,
                            position=Vec3(0.7,-1,1.5),
                            rotation=Vec3(0,170,0),
                            model="assets/3d-models/stabby_item.obj",
                            texture="assets/texture/stabby_final.png",
                            visible=False)

        self.itemList = [self.cube,self.chainItem,self.stabby]
        self.currentItem = 0
        self.switchItems()
        self.stabbing = False
        self.stabbingCounter = False
        self.lastActivaed = 0
        self.healthBar = HealthBar(max_value=100)
        self.isPlayer = True

    def switchItems(self):
        for i,v in enumerate(self.itemList):
            if i == self.currentItem:
                v.visible = True
            else:
                v.visible = False
    
    def input(self,key):
        try:
            self.currentItem = int(key) - 1
            self.switchItems()
        except ValueError:
            pass

        if key == "scroll up":
            self.currentItem = (self.currentItem + 1) % len(self.itemList)
            self.switchItems()
        
        if key == "r":
            self.controller.position = Vec3(0,0,0)

        if mouse.left and self.currentItem == 2:
            if self.stabbingCounter:
                if misc.cooldown(lastActivated=self.lastActivaed,cooldown=0.5):
                    self.stabbing = True
                    self.lastActivaed = int(time.time())
            else:
                self.lastActivaed = int(time.time())
                self.stabbing = True
                self.stabbingCounter = True

    def update(self):
        self.controller.camera_pivot.y = 2 - held_keys["left control"]
