from ursina import *
import numpy as np


def update():
    global t
    t = t + 0.01
    angle = np.pi*40/180
    
    radius = 1
    n = 0
    pd = 4
    mercury.y = np.cos(pd*t+angle*n)*radius
    mercury.z = np.sin(pd*t+angle*n)*radius    

    radius = 1.4
    n = 1
    pd = 3
    venus.y = np.cos(pd*t+angle*n)*radius
    venus.z = np.sin(pd*t+angle*n)*radius
    venus.x = venus.y*np.sin(angle*n)
    venus.y = venus.y*np.cos(angle*n)

    radius = 1.8
    n = 2
    pd = 2
    earth.y = np.cos(pd*t+angle*n)*radius
    earth.z = np.sin(pd*t+angle*n)*radius  
    earth.x = earth.y*np.sin(angle*n)    
    earth.y = earth.y*np.cos(angle*n)

    radius = 2.2
    n = 3
    pd = 1
    mars.y = np.cos(pd*t+angle*n)*radius
    mars.z = np.sin(pd*t+angle*n)*radius
    mars.x = mars.y*np.sin(angle*n)    
    mars.y = mars.y*np.cos(angle*n)

    radius = 2.6
    n = 4
    pd = 3
    jupiter.y = np.cos(pd*t+angle*n)*radius
    jupiter.z = np.sin(pd*t+angle*n)*radius
    jupiter.x = jupiter.y*np.sin(angle*n)
    jupiter.y = jupiter.y*np.cos(angle*n)
    
    radius = 3
    n = 5
    pd = 5
    saturn.y = np.cos(pd*t+angle*n)*radius
    saturn.z = np.sin(pd*t+angle*n)*radius
    saturn.x = saturn.y*np.sin(angle*n)        
    saturn.y = saturn.y*np.cos(angle*n)

    radius = 3.4
    n = 6
    pd = 2
    uranus.y = np.cos(pd*t+angle*n)*radius
    uranus.z = np.sin(pd*t+angle*n)*radius
    uranus.x = uranus.y*np.sin(angle*n)
    uranus.y = uranus.y*np.cos(angle*n)

    radius = 3.8
    n = 7
    pd = 5
    neptune.y = np.cos(pd*t+angle*n)*radius
    neptune.z = np.sin(pd*t+angle*n)*radius 
    neptune.x = neptune.y*np.sin(angle*n)
    neptune.y = neptune.y*np.cos(angle*n)

    radius = 4
    n = 8
    pd = 4
    pluto.y = np.cos(pd*t+angle*n)*radius
    pluto.z = np.sin(pd*t+angle*n)*radius
    pluto.x = pluto.y*np.sin(angle*n)    
    pluto.y = pluto.y*np.cos(angle*n)    

app = Ursina()

sun = Entity(model='sphere',color=color.yellow, scale=1.5)

mercury = Entity(model='sphere',color=color.gray, scale=0.2)
venus = Entity(model='sphere',color=color.orange, scale=0.3)
earth = Entity(model='sphere',color=color.blue, scale=0.4)
mars = Entity(model='sphere',color=color.violet, scale=0.3)
jupiter = Entity(model='sphere',color=color.red, scale=0.6)
saturn = Entity(model='sphere',color=color.white, scale=0.5)
uranus = Entity(model='sphere',color=color.cyan, scale=0.5)
neptune = Entity(model='sphere',color=color.gold, scale=0.5)
pluto = Entity(model='sphere',color=color.pink, scale=0.2)

t = -np.pi

#camera.position=(0,25,0)
#camera.rotation_x=90

app.run()
