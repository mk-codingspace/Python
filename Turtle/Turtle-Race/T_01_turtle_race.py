# import module
import turtle
from random import randint

# set up screen
width = 700
height = 500
S = turtle.Screen()
S.setup(width,height)
S.bgcolor('lightgreen')

# Create pen
#T = turtle.Turtle()
T = turtle.Pen()
T.speed(0)

# Start line
T.up()
T.setposition(-140,50)
T.write('Start line',align='center')
T.right(90)
T.forward(10)
T.down()
T.forward(155)

# Finish line
T.up()
T.setposition(140,50)
T.write('Finish line',align='center')
T.forward(10)
T.down()
T.forward(155)

# Tracks
T.up()
T.setposition(-170,20)
T.color('white')
T.down()
T.left(90)
T.forward(340)

T.up()
T.setposition(-170,-5)
T.down()
T.forward(340)

T.up()
T.setposition(-170,-35)
T.down()
T.forward(340)

T.up()
T.setposition(-170,-65)
T.down()
T.forward(340)

T.up()
T.setposition(-170,-95)
T.down()
T.forward(340)

T.hideturtle()

# 1st turtle, red
T1 = turtle.Turtle()
T1.up()
T1.setposition(-160,10)
T1.shape('turtle')
T1.color('red')

# 2nd turtle, green
T2 = turtle.Turtle()
T2.up()
T2.setposition(-160,-20)
T2.shape('turtle')
T2.color('green')

# 3rd turtle, blue
T3 = turtle.Turtle()
T3.up()
T3.setposition(-160,-50)
T3.shape('turtle')
T3.color('blue')

# 4th turtle, yellow
T4 = turtle.Turtle()
T4.up()
T4.setposition(-160,-80)
T4.shape('turtle')
T4.color('yellow')

# race
line = 140
while T1.xcor() < line or T2.xcor() < line or T3.xcor() < line or \
      T4.xcor() < line:
    T1.forward(randint(1,5))
    T2.forward(randint(1,5))
    T3.forward(randint(1,5))
    T4.forward(randint(1,5))

# Decide ranking
finals_list = [T1.xcor(),T2.xcor(),T3.xcor(),T4.xcor()]
finals_dict = {T1.xcor():'red', T2.xcor():'green', \
               T3.xcor():'blue',T4.xcor():'yellow'}


finals_list = sorted(finals_list,reverse=True) 

# Ranking board
T.up() 
T.color('Black')
T.setposition(-60,200)
T.write('Ranking Board',align='left', font=(None,12))

# 1st
T.setposition(-60,180)
rank = finals_list[0]
T.write(f'1st place: {finals_dict[rank]} turtle',align='left')

# 2nd
T.setposition(-60,160)
rank = finals_list[1]
T.write(f'2nd place: {finals_dict[rank]} turtle',align='left')

# 3rd
T.setposition(-60,140)
rank = finals_list[2]
T.write(f'3rd place: {finals_dict[rank]} turtle',align='left')

# 4th
T.setposition(-60,120)
rank = finals_list[3]
T.write(f'4th place: {finals_dict[rank]} turtle',align='left')

