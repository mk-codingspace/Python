# Press "r", "p", or "s" button to play for the game 

# Import modules
import turtle
import random

def update_scoreP():
    global scoreP
    scoreP += 1
    penP.clear()
    penP.write(f"You: {scoreP}",align="center", font = (None,20))
    
def update_scoreC():
    global scoreC
    scoreC += 1
    penC.clear()
    penC.write(f"Computer: {scoreC}",align="center", font = (None,20))

# Functions
def rock():
    player.shape(rock_img)
    ind = random.randint(0,2)
    computer.shape(images[ind])
    if ind == 1: # Paper
        update_scoreC()
    elif ind==2: # scissors
        update_scoreP()
    
def paper():
    player.shape(paper_img)
    ind = random.randint(0,2)
    computer.shape(images[ind])
    if ind == 0: # rock
        update_scoreP()
    elif ind==2: # scissors
        update_scoreC()

def scissors():
    player.shape(scissors_img)    
    ind = random.randint(0,2)
    computer.shape(images[ind])
    if ind == 0: # rock
        update_scoreC()
    elif ind==1: # paper
        update_scoreP()
    
# window
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.setup(width = 600,height = 500)
wn.title("Rock Paper Scissors")

# Draw center line
T = turtle.Turtle()
T.speed(0)
T.up()
T.setposition(0,-250)
T.down()
T.color("white")
T.pensize(3)
T.left(90)
T.forward(600)

# register shape images
rock_img = 'images/rock.gif'
paper_img = 'images/paper.gif'
scissors_img = 'images/scissors.gif'
images =[rock_img,paper_img,scissors_img]

turtle.register_shape(rock_img)
turtle.register_shape(paper_img)
turtle.register_shape(scissors_img)

# Create the player turtle, and initialize the image to be rock
player = turtle.Turtle()
player.shape(rock_img)
player.up()
player.speed(0)
player.setposition(-150,-50)

# Create the computer turtle, and initialize the image to be rock
computer = turtle.Turtle()
computer.shape(rock_img)
computer.up()
computer.speed(0)
computer.setposition(150,-50)

# keyboard binding
wn.listen()
wn.onkey(rock,"r")
wn.onkey(paper,"p")
wn.onkey(scissors,"s")

# Initilize scores
scoreP = 0
scoreC = 0

# Score board
penP = turtle.Turtle()
penP.speed(0)
penP.up()
penP.hideturtle()
penP.goto(-150,150)
penP.write("You: 0",align="center", font = (None,20))

penC = turtle.Turtle()
penC.speed(0)
penC.up()
penC.hideturtle()
penC.goto(150,150)
penC.write("Computer: 0",align="center", font = (None,20))

