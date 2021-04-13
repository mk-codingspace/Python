from ursina import *
import math

def update():
    global speed
    length = 3

    factor = -0.0009 
    for i in range(10):    
        angle = math.asin((pendulums[i].x)/length)    
        acceleration = factor * math.sin(angle)
        speed[i] += acceleration
        angle += speed[i]
        pendulums[i].x = length * math.sin(angle)
        pendulums[i].y = 0 - length * math.cos(angle)

        factor += 0.00001 

app = Ursina() 
speed = [0]*10
pendulums= [None]*10

for i in range(10):
    pendulums[i] = Entity(model='sphere', color=color.random_color(), scale = 0.3, position=(2.5,2,i*2))
 

camera.position=(0,-1.5,-20)

app.run()
