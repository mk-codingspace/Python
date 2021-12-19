from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

def update():
    global Bats,Monsters, run_bat, run_monster
    if run_bat:
        for b in Bats:
            b.z -= 0.1
            if b.z <= -20:
                Bats.remove(b)
                destroy(b)
        for m in Monsters:
            Monsters.remove(m)
            destroy(m)
            
    if run_monster:
        for m in Monsters:
            m.z -= 0.1
            if m.z <= -20:
                Monsters.remove(m)
                destroy(m)
        for b in Bats:
            Bats.remove(b)
            destroy(b)

def input(key):
    global Bats, Monsters, run_bat, run_monster
    if not run_bat:
        if key == '1':
            run_bat = True
            run_monster = False
            invoke(new_bat,delay=0.1)

    if not run_monster:        
        if key == '2':
            run_monster = True
            run_bat = False                
            invoke(new_monster,delay=0.1) 
        
    if key=="left mouse down":
            Audio("assets/laser_sound.wav")
            Animation("assets/spark", parent=camera.ui, fps=5,
                      scale=.1, position=(.19, -.03), loop=False)
            for b in Bats:
                if b.hovered:
                    b.z = -19
            for m in Monsters:
                if m.hovered:
                    m.z=-19            

def new_bat():
    global Bats, run_bat
    new= Animation(
        'assets//bat',
        collider = 'box',
        position = (-11,2,20),
        scale = (1.3,0.8),
        )
    Bats.append(new)
    if run_bat:
        invoke(new_bat,delay = random.uniform(1,3))
    
def new_monster():
    global Monsters, run_monster
    new = Animation(
        'assets//tentakelding',
        collider = 'box',
        position = (-11,2,20),
        scale = (1.3,0.8),
        )
    Monsters.append(new)
    if run_monster:
        invoke(new_monster,delay = random.uniform(1,3))

app=Ursina()
Sky()

player=FirstPersonController(y=2, origin_y=-.5)
ground=Entity(model='plane', scale=(100, 1, 100), color=color.lime, texture="white_cube",
	texture_scale=(100, 100), collider='box')


wall_1=Entity(model="cube", collider="box", position=(-8, 0, 20), scale=(.5,8,30), rotation=(0,0,0),
	texture="brick", texture_scale=(5,5), color=color.rgb(255, 128, 0))

wall_2=duplicate(wall_1, x=-15)

gun=Entity(model="assets/gun.obj", parent=camera.ui, scale=.08, color=color.gold, position=(.3, -.2),
	rotation=(-5, -10, -10))

bat = Entity(model='circle',scale=0.01)
monster = duplicate(bat)
run_bat = False
run_monster = False

Bats=[bat]
Monsters =[monster]

app.run()
