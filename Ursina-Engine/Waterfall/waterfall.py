from ursina import *
import numpy as np

def update():
    global e1,e2,e3,e4,e5
    speed = 0.005

    angle = 0
    for entity in e1:
        radius = entity.x/np.cos(angle)
        radius -= speed       
        entity.x = radius*np.cos(angle)
        entity.z = radius*np.sin(angle)
        entity.y = -3/abs(entity.x) +3   
        if radius < 0.3:
            entity.x = 4*np.cos(angle)
            entity.z = 4*np.sin(angle)
            entity.y = -3/abs(entity.x/np.cos(angle))+3   

    angle = 60/180*np.pi
    for entity in e2:
        radius = entity.x/np.cos(angle)
        radius -= speed        
        entity.x = radius*np.cos(angle)
        entity.z = radius*np.sin(angle)
        entity.y = -3/abs(entity.x/np.cos(angle))+3   
        if radius < 0.3:
            entity.x = 4*np.cos(angle)
            entity.z = 4*np.sin(angle)
            entity.y = -3/abs(entity.x/np.cos(angle))+3   

    angle = 90/180*np.pi
    for entity in e3:
        radius = entity.x/np.cos(angle)
        radius -= speed        
        entity.x = radius*np.cos(angle)
        entity.z = radius*np.sin(angle)
        entity.y = -3/abs(entity.x/np.cos(angle))+3   
        if radius < 0.3:
            entity.x = 4*np.cos(angle)
            entity.z = 4*np.sin(angle)
            entity.y = -3/abs(entity.x/np.cos(angle))+3   

    angle = 120/180*np.pi
    for entity in e4:
        radius = entity.x/np.cos(angle)
        radius -= speed       
        entity.x = radius*np.cos(angle)
        entity.z = radius*np.sin(angle)
        entity.y = -3/abs(entity.x/np.cos(angle))+3   
        if radius < 0.3:
            entity.x = 4*np.cos(angle)
            entity.z = 4*np.sin(angle)
            entity.y = -3/abs(entity.x/np.cos(angle))+3   

    angle = 180/180*np.pi
    for entity in e5:
        radius = entity.x/np.cos(angle)
        radius -= speed        
        entity.x = radius*np.cos(angle)
        entity.z = radius*np.sin(angle)
        entity.y = -3/abs(entity.x/np.cos(angle))+3   
        if radius < 0.3:
            entity.x = 4*np.cos(angle)
            entity.z = 4*np.sin(angle)
            entity.y = -3/abs(entity.x/np.cos(angle))+3   
                   
app = Ursina()

num = 40
radius = np.linspace(4,0.3,num)

angle = 0
x1 = radius*np.cos(angle)
z1 = radius*np.sin(angle)
y1 = -3/abs(x1) + 3

angle = 60/180*np.pi
x2 = radius*np.cos(angle)
z2 = radius*np.sin(angle)
y2 = y1

angle = 90/180*np.pi
x3 = radius*np.cos(angle)
z3 = radius*np.sin(angle)
y3 = y1

angle = 120/180*np.pi
x4 = radius*np.cos(angle)
z4 = radius*np.sin(angle)
y4 = y1

angle = 180/180*np.pi
x5 = radius*np.cos(angle)
z5 = radius*np.sin(angle)
y5 = y1

e1= [None]*num
e2= [None]*num
e3= [None]*num
e4= [None]*num
e5= [None]*num

for i in range(num):
    e1[i] = Entity(model="sphere",color=color.red,
                  scale=0.1,position=(x1[i],y1[i],z1[i]))
    e2[i] = Entity(model="sphere",color=color.yellow,
                  scale=0.1,position=(x2[i],y2[i],z2[i]))
    e3[i] = Entity(model="sphere",color=color.white,
                  scale=0.1,position=(x3[i],y3[i],z3[i]))
    e4[i] = Entity(model="sphere",color=color.cyan,
                  scale=0.1,position=(x4[i],y4[i],z4[i]))
    e5[i] = Entity(model="sphere",color=color.green,
                  scale=0.1,position=(x5[i],y5[i],z5[i]))

Text(text='Funnel Waterfall',position=(0,0.4),origin=(0,0),background=True)
app.run()

