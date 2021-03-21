from ursina import *
from random import randint

def update():
    global score
    basket.x = basket.x + held_keys['right arrow']*time.dt*basket_dx
    basket.x = basket.x - held_keys['left arrow']*time.dt*basket_dx

    apple.y = apple.y + time.dt* apple_dy
    
    hit_info = apple.intersects()
    if hit_info.hit:
        Audio('sounds/thud.wav')
        apple.x = randint(-4,4)
        apple.y = 4
        score = score + 1
        print_on_screen(f"Apple caught: {score}",position=(-0.8,.45), scale=1, duration=2)

    if apple.y < -4:
        Audio('sounds/lost.wav')
        print_on_screen("You lose. Let's restart!",position=(0,0),origin=(0,0),scale=2, duration=2)
        score = 0
        apple.x = randint(-4,4)
        apple.y = 10    

  
app=Ursina()

left_wall = Entity(model='quad',color=color.green,scale=(0.6,10),position=(-7,0,0),collider='box')
right_wall = duplicate(left_wall,x=7)

apple = Entity(model='quad',texture ='img/apple.png',position=(randint(-4,4),10),collider='box')
basket = Entity(model='quad',texture='img/basket.png',position=(0,-4),collider='box')

basket_dx = 5
apple_dy = -2
score = 0

app.run()

    
