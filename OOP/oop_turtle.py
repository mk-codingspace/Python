import turtle

WIDTH = 700
HEIGHT = 500
S = turtle.Screen()
S.setup(WIDTH,HEIGHT)
S.title("Learn OOP through graphics")

class Shape:
    def __init__(self,shape,color,x,y,heading,speed):
        size = 2
        self.T = turtle.Pen()

        self.T.shapesize(size)
        self.T.shape(shape)
        self.T.color(color)
        self.T.up()
        self.T.setpos(x,y)
        self.T.setheading(heading)
        self.speed = speed

    def move(self):
        self.T.forward(self.speed)
        if abs(self.T.xcor()) >= WIDTH //2 or abs(self.T.ycor()) >= HEIGHT//2:
            self.speed *= -1
        

# create objects
obj_1 = Shape('turtle','red',-100,-100,0,5)
obj_2 = Shape('circle','green',-100,100,90,10)
obj_3 = Shape('square','blue',100,-100,180,3)
obj_4 = Shape('triangle','black',100,100,270,8)

while True:
    obj_1.move()
    obj_2.move()
    obj_3.move()
    obj_4.move()

turtle.mainloop()
