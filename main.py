from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import scriptsToImport.player as player
import scriptsToImport.jsonHandler as jsonHandler 
import scriptsToImport.chainEntity as chainEntity
import time

seconds = time.time()
app = Ursina()
coordsDisplay = Text(text="Coords will be here",
                     position=Vec2(-.5,.5))

config = jsonHandler.openJson("system-files\config.json")
window.fullscreen = config["fullScreen"]
window.title = "Amongus but better"
coordsDisplay.visible = config["coordsDisplay"]
if config["editorCam"]:
    EditorCamera()
skyTexture = load_texture("assets/texture/sky.gif")
Sky(texture=skyTexture)

ground = Entity(
    model = 'cube',
    color = color.magenta,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (50, 1, 10),
    collider = 'box'
    )

#EditorCamera()
playerEntity = player.Player()
chainTest = chainEntity.chainEntity()
chainTest.visible = True

counterVar = False

def update():
    global counterVar
    global lastActivated
    if held_keys["escape"]:
        quit()
    if mouse.right:
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
    coordsDisplay.text = f"X: {round(playerEntity.world_position.x)} Y: {round(playerEntity.world_position.y)} Z: {round(playerEntity.world_position.z)}"

app.run()  