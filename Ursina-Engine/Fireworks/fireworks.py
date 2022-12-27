from ursina import *
from random import randint, uniform, choice

class Fireworks(Entity):
    def __init__(self,x,y,color):
        super().__init__()
        self.parent=camera.ui
        self.model="circle"
        self.color=color
        self.scale= 0.02 #.012
        self.x=x
        self.y=y
        self.dx=randint(-2,2)/1000
        self.dy=randint(-2,2)/1000
        self.ds=randint(1,3)/7000

    def update(self):
        self.x +=self.dx
        self.y +=self.dy
        self.scale -=self.ds
        if self.scale <=.005:
            destroy(self)
            
def CreateFireworks():
    num = 12
    e =[None]*num
    x=uniform(-0.45,0.45)
    y=uniform(0,0.4)
    c=choice(colors)
    for i in range(num):
        e[i]=Fireworks(x, y,c)
    Audio('assets/explosion_sound.wav')
    invoke(CreateFireworks, delay=uniform(0.1,0.8))

app = Ursina()

window.color=color.black
Text("Happy New Year!",origin=(0,1.5), scale=5,color=color.yellow)
colors =[color.white,color.green,color.yellow,color.pink,color.cyan,
         color.red,color.gold,color.violet]
CreateFireworks()

app.run()
