import turtle

# set up screen
width = 500
height = 500
S = turtle.Screen()
S.setup(width,height)
S.title('Flashing Christmas Tree. Merry Christmas!')

# Create pen
T = turtle.Pen()
T.speed(0)

# Top triangle
T.up()
T.setposition(-60,100)
T.down()
T.fillcolor('green')
T.begin_fill()
T.fd(120)
T.lt(130)
T.fd(95)
T.lt(100)
T.fd(95)
T.end_fill()

# Middle trapezoid
T.setx(-35)
T.fillcolor('green')
T.begin_fill()
T.fd(100)
T.lt(130)
T.fd(200)
T.lt(130)
T.fd(100)
T.end_fill()

# Bottom trapezoid
T.up()
T.setposition(-45,24)
T.down()
T.fillcolor('green')
T.begin_fill()
T.lt(100)
T.fd(130)
T.lt(130)
T.fd(260)
T.lt(130)
T.fd(130)
T.end_fill()

# Trunk
T.up()
T.setposition(-30,-75)
T.down()
T.fillcolor('brown')
T.begin_fill()
T.lt(140)
T.fd(50)
T.lt(90)
T.fd(60)
T.lt(90)
T.fd(50)
T.end_fill()

# Star on the top
T.up()
T.setposition(-30,190)
T.rt(90)
T.down()
T.fillcolor('yellow')
T.begin_fill()
for i in range(5):
    T.fd(60)
    T.rt(144)
T.end_fill()
T.hideturtle()

# Three Lights
colors = ['red','yellow','cyan']

T1 = turtle.Pen()
T2 = turtle.Pen()
T3 = turtle.Pen()

T1.up()
T1.setposition(0,-20)
T1.down()
T1.hideturtle()

T2.up()
T2.setposition(0,60)
T2.down()
T2.hideturtle()

T3.up()
T3.setposition(0,130)
T3.down()
T3.hideturtle()

# static light
##T1.dot(20,'red')
##T2.dot(20,'yellow')
##T3.dot(20,'cyan')

# Flashing light
m = 0
while True:
    T1.dot(20,colors[m%3]) #0,1,2,0,1,2,0,1,2,...
    T2.dot(20,colors[(m+1)%3]) #1,2,0,1,2,0,1,2,0,...
    T3.dot(20,colors[(m+2)%3]) #2,0,1,2,0,1,2,0,1,...
    m=m+1


