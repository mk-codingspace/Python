# Matrix digital rain
from ursina import *

def update():
    for entity in cubes:
        entity.rotation_y += time.dt * 5                # Rotate all the cubes every time update is called

    global offset, offset2
    offset = offset + time.dt * 0.3                     # Add a small number to this variable
    offset2 = offset2 + time.dt * 0.4                   # Add a value to this variable, but different to the first one

    setattr(cube, "texture_offset", (0, offset))  # Assign as a texture offset
    setattr(cube2, "texture_offset", (0, offset2)) 

app=Ursina()

cubes=[]
cube = Entity(model='cube', scale=(7,5,6), texture="img/digit_rain.png")
cubes.append(cube)                                  # Add the cube to the list
cube2 = Entity(model='cube', color=color.rgba(255,255,255,128), scale=(7.5,5,6.5),
               texture="img/digit_rain.png")

cubes.append(cube2)

offset = 0
offset2 = 0

app.run()
