from ursina import *
from ursina.prefabs.health_bar import HealthBar

app = Ursina()

health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=50)
print(health_bar_1.text_entity.enabled, health_bar_1.text_entity.text)

def input(key):
    if key == '+' or key == '+ hold':
        health_bar_1.value += 10
    if key == '-' or key == '- hold':
        health_bar_1.value -= 10
        print('ow')

app.run()