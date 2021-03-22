from ursina import *

def update():
    global dx,dz,score_A,score_B

    paddle_A.x = paddle_A.x + held_keys['d']*time.dt
    paddle_A.x = paddle_A.x - held_keys['a']*time.dt

    paddle_B.x = paddle_B.x + held_keys['right arrow']*time.dt
    paddle_B.x = paddle_B.x - held_keys['left arrow']*time.dt

    ball.x = ball.x + time.dt*dx
    ball.z = ball.z + time.dt*dz

# Boundary checking
    # Left and right
    if abs(ball.x) > 0.4:
        dx = -dx

    # Top and Bottom
    if ball.z > 0.25:
        Audio('sounds/whistle.wav')
        score_B = score_B + 1
        print_on_screen(f"Player A : Player B = {score_A} : {score_B}",position=(-0.85,.45), scale=2, duration=2)
        reset()

    if ball.z < -0.65:
        Audio('sounds/whistle.wav')
        score_A = score_A + 1
        print_on_screen(f"Player A : Player B = {score_A} : {score_B}",position=(-0.85,.45), scale=2, duration=2)      
        reset()

    # Collisions    
    hit_info = ball.intersects()    
    if hit_info.hit:
        if hit_info.entity == paddle_A or hit_info.entity == paddle_B:
            Audio('sounds/pong_sound.wav')
            dz = -dz

def reset():
    ball.x=0
    ball.z=-0.20  
    
app=Ursina()
window.color = color.orange

table = Entity(model='cube',color=color.green,scale=(10,0.5,14),
                 position=(0,0,0),texture="white_cube")

paddle_A = Entity(parent=table,color=color.black, model='cube',scale=(0.20,0.03,0.05),
                  position=(0,3.7,0.22),collider='box')
paddle_B = duplicate(paddle_A, z=-0.62)

Text(text="Player A",scale=2, position=(-0.1,0.32))
Text(text="Player B",scale=2, position=(-0.1,-0.4))

line = Entity(parent=table, model='quad',scale=(0.88,0.2,0.1),position=(0,3.5,-0.20))
ball = Entity(parent=table,model='sphere',color=color.red,scale=0.05,
              position=(0,3.71,-0.20),collider='box')

dx=0.1
dz = 0.2
score_A = 0
score_B = 0

camera.position = (0, 15, -26)
camera.rotation_x = 30

app.run()
