from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import scriptsToImport.player as player
import scriptsToImport.chainEntity as chainEntity
import scriptsToImport.misc as misc
import time
import scriptsToImport.enemy as enemy

seconds = time.time()
app = Ursina()
coordsDisplay = Text(text="Coords will be here",
                     position=Vec2(-.5,.5))

config = misc.openJson("system-files\config.json")
window.fullscreen = config["fullScreen"]
window.title = "Amongus but better"
coordsDisplay.visible = config["coordsDisplay"]
if config["editorCam"]:
    EditorCamera()
skyTexture = load_texture("assets/texture/sky.gif")
Sky(texture=skyTexture)

ground = Entity(
    model = 'cube',
    origin = (0, .5),
    scale = 100,
    collider = 'box',
    texture="grass"
    )

playerEntity = player.Player()
chainTest = chainEntity.chainEntity()
chainTest.visible = True
enemyIgnoreList = []
lastSummoned = 0
summonChecker = False

counterVar = False

def update():
    global summonChecker
    global lastSummoned
    global counterVar
    global lastActivated

    if held_keys["escape"]:
        quit()
    if mouse.left:
        if playerEntity.currentItem == 1:
            if not counterVar:
                chainEntity.shootOut(playerEntity.world_rotation,playerEntity.world_position,ignoreEntity=[playerEntity])
                lastActivated = time.time()
                counterVar = True
            elif counterVar:
                now = time.time()
                if now - lastActivated >= 3:
                    chainEntity.shootOut(playerEntity.world_rotation,playerEntity.world_position,ignoreEntity=[playerEntity])
                    lastActivated = time.time()
    
    if playerEntity.stabbing:
        playerEntity.stabby.rotation_x += 5
        if playerEntity.stabby.rotation_x == 330:
            playerEntity.stabbing = False
            playerEntity.stabby.rotation = Vec3(0,170,0)
    
    if held_keys["e"]:
        if not summonChecker:
            enemyIgnoreList.append(enemy.Enemy(listToIgnore=enemyIgnoreList,target=playerEntity))
            lastSummoned = int(time.time())
            summonChecker = True 
        else:
            if misc.cooldown(lastActivated=lastSummoned,cooldown=1):
                enemyIgnoreList.append(enemy.Enemy(listToIgnore=enemyIgnoreList,target=playerEntity))
                lastSummoned = int(time.time())

    coordsDisplay.text = f"X: {round(playerEntity.world_position.x)} Y: {round(playerEntity.world_position.y)} Z: {round(playerEntity.world_position.z)}"
    
app.run()  