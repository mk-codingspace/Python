from ursina import *
import random    
        
def update():
    global offset, run

    if run:
        # Rolling background
        offset += time.dt * 0.3
        setattr(road, "texture_offset", (0,offset))

        car.x += held_keys['d'] * time.dt * 0.5
        car.x -= held_keys['a'] * time.dt * 0.5

        if car.x >= 0.24:
            car.x = 0.24
        if car.x <= -0.28:
            car.x = -0.28

        for pumpkin in pumpkins:
            pumpkin.z -= time.dt * 0.3
            
            if  pumpkin.z <= -20:
                pumpkins.remove(pumpkin)
                destroy(pumpkin)

            if abs(car.x-pumpkin.x) <0.1:
                if abs(car.z-pumpkin.z) <0.05:
                    invoke(crash,delay=1)
                    run = False
                    
def NewPumpkin():
    scale = (2,1,1)
    fac = random.uniform(0.02,0.2)
    s = [ele*fac for ele in scale]
    x= random.uniform(-0.28,0.24)
    z= random.uniform(0.45,0.60)
    new = duplicate(pumpkin,scale=s,x=x,z=z,
                    texture = random.choice(textures))
    pumpkins.append(new)
    invoke(NewPumpkin,delay = random.uniform(1,3))
            
def crash():
    Text(text='Crashed! Reload the game!',origin=(0,0), scale=3,
         color=color.yellow,background=True)

app=Ursina()
window.color = color.orange
run = True
offset = 0

textures = ['pumpkin_Color','pumpkin_Normal','pumpkin_Roughness']
textures = ['assets/' + s for s in textures]

road = Entity(model='cube',color=color.green,scale=(10,0.5,60),
                 position=(0,0,0),texture="assets/road.png")

car = Entity(parent= road, model='cube',texture='assets/car.png',
            scale = (0.17,0.0001,0.06),position=(-0.07,1,-0.12),
            collider = 'box')

pumpkin = Entity(
    parent = road,
    rotation_x = 45,
    model='assets/pumpkin.obj',
    scale =(0.2,0.1,0.1),
    position = (0,0.99,0.5),
    texture = random.choice(textures),
    collider = 'box'
    )

pumpkins=[]
NewPumpkin()

camera.position = (0, 8, -26)
camera.rotation_x = 20
app.run()
