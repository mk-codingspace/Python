from ursina import *

app=Ursina()

rock = Entity(model='quad',scale= 2, position=(0,-1,-0.5),
              texture='assets/rock.png')
mk = Entity(model='quad',position=(0,-1.7,10),texture='assets/monkey_king.png')

def input(key):
    if key == 'space':
        Audio('assets/explosion_effect.mp3')
        Animation('assets/explosion', position=(0,-1),
                        scale=(3,3), fps=6,loop=False, autoplay=True)
        destroy(rock)

        mk.animate_position((2,2,0),duration=5,loop=False)
        mk.animate_scale(4,duration=5,loop=False)


app.run()
