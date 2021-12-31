# import module
import turtle
from random import randint, choice

# set up screen
width = 700
height = 500
S = turtle.Screen()
S.setup(width,height)
S.bgcolor('black')
S.title("Fireworks")

# colors
colors =['red','green','yellow','gold','pink','cyan','white','orange',
         'violet','coral']

class Fireworks:
    def __init__(self,radius):
        self.T = turtle.Pen()
        self.T.speed(0)
        self.T.color(choice(colors))
        self.T.hideturtle()
        self.T.up()
        self.T.setposition(randint(-250,250),randint(0,200))
        self.T.down()
        self.radius = radius

    def update(self):
        self.T.forward(self.radius)
        self.T.backward(self.radius)
        self.T.left(10)

    def clean(self):
        self.T.clear()
        self.T.color(choice(colors))
        self.T.up()
        self.T.setposition(randint(-250,250),randint(0,200))
        self.T.down()        

# Objects
T1 = Fireworks(randint(10,100))
T2 = Fireworks(randint(10,100))
T3 = Fireworks(randint(10,100))
T4 = Fireworks(randint(10,100))
T5 = Fireworks(randint(10,100))
    
##
T = turtle.Pen()
T.sety(-150)
T.color('gold')
T.write('Happy New Year!',align='center',font=(None,50))
T.hideturtle()

while True:
        
    for i in range(36):
        T1.update()
        T2.update()
        T3.update()
        T4.update()        
        T5.update()
        
    T1.clean()
    T2.clean()
    T3.clean()
    T4.clean()   
    T5.clean()

turtle.mainloop()
