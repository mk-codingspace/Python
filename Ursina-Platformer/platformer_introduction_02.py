from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

size = 13
bg = Entity(model='quad', scale=(size,6), texture='assets/sky_cloud',z=0.5)
for m in range(2):
    duplicate(bg, x=size*(m+1))
    duplicate(bg, x=-size*(m+1))

player = PlatformerController2d(y=1, scale_y=1,color=color.green)

ground = Entity(model='quad', y=-2, scale_x=10, collider='box', color=color.yellow)
duplicate(ground, x=size)
duplicate(ground, x=-size)

wall = Entity(model='quad', color=color.azure, scale=(1,3), x=5.5, collider='box')
duplicate(wall, x=5.5+size)
duplicate(wall, x=5.5-size)

level = Entity(model='quad', color=color.red, scale=(3,1), x=2, collider='box')
duplicate(level, x=2+size)
duplicate(level, x=2-size)


ceiling = Entity(model='quad', color=color.cyan, scale=(3,1), x=-2.5, y=1,
                 collider='box')
duplicate(ceiling, x=-2.5+size)
duplicate(ceiling, x=-2.5-size)

camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))
#camera.z = -30

app.run()
