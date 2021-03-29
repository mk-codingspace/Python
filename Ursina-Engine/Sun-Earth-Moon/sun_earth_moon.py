# Basic cube

from ursina import * # import ursina engine

def update():
    for entity in entities:                             # Go through the cube list
        entity.rotation_y += time.dt * 100           # Rotate all the cubes every time update is called


def input(key):

    if key == '1':
        camera.position = (0, 0, -20)
        camera.rotation_x = 0

    if key == '2':
        camera.position = (0, 20, 0)
        camera.rotation_x = 90

    if key == '3':
        camera.position = (0, 10, -17.33)
        camera.rotation_x = 30
    
app = Ursina() # Initialize your Ursina app

entities = [] 
sun = Entity(model='sphere', color=color.yellow, scale=2)
earth = Entity(parent=sun, model='sphere', color=color.green,
        position=(1, 0, 1), scale=0.4)
moon = Entity(parent=earth, model='sphere', color=color.white,
        position=(0.5, 0, 0.5), scale=0.3)

entities.append(sun)
entities.append(earth)
entities.append(moon)

app.run() # Run the app
