from ursina import *
from random import randint

class Pipe(Entity):
    def __init__(self,x,y,img):
        super().__init__()
        self.model = 'quad'
        self.scale = (1,7)
        self.color = color.green
        self.x = x
        self.y = y
        self.texture = img
        self.collider = 'box'
        self.score_tag = True

def update():
    global offset, run, n_frame, score, text

    if run:
        # Sound
        n_frame += 1
        if n_frame > 100:
            Audio('assets/bird_chirp.mp3')
            n_frame = 0
     
        # Rolling background
        offset += time.dt * 0.3 
        setattr(bg, "texture_offset", (offset,0))

        for m in range(num):
            pipes_top[m].x -= time.dt * 1.8
            pipes_bottom[m].x -= time.dt * 1.8

            if pipes_top[m].x < -8:
                pipes_top[m].x += 4*num
                pipes_bottom[m].x += 4*num
                pipes_top[m].score_tag = True

            if pipes_top[m].x < bird.x and pipes_top[m].score_tag:
                score += 1
                text.y = 1
                text=Text(text=f"Score: {score}",position=(-0.65,0.4),origin=(0,0),scale=2,color=color.yellow,background=True) 
                pipes_top[m].score_tag = False          
                
        # Collision
        hit_info = bird.intersects()
        if hit_info.hit:
            run = False
            invoke(Func(bird.shake, duration =2))
            invoke(Func(bird.fade_out, duration =3))
            invoke(crash, delay = 3)

def crash():
    Text(text='Crashed! Reload the game!',origin=(0,0), scale=3,color=color.red)

def input(key):
    if key == "up arrow" or key == "up arrow hold":
        bird.y += 0.25
    if key == "down arrow" or key == "down arrow hold":
        bird.y -= 0.25

# Main code
app = Ursina()

# Some variables
offset = 0
run = True
n_frame = 0
num = 5
x = 6
score = 0

bg = Entity(model='quad', scale=(20,10), texture='assets/bg',z=0.1)

bird = Animation(
    'assets//bird',
    collider = 'box',
    scale = (1.3,0.8),
    y = 1.5
    )

pipes_bottom = [None]*num
pipes_bottom[0]=Pipe(x,-4,'assets/pipe_bottom.png')

pipes_top = [None]*num
pipes_top[0]=Pipe(x,-4+9,'assets/pipe_top.png')

for m in range(1,num):

    x += 4
    y = -7 + randint(0,50)/10    
    pipes_bottom[m]=Pipe(x,y,'assets/pipe_bottom.png')
    pipes_top[m]=Pipe(x,y+9,'assets/pipe_top.png')

text=Text(text=f"Score: {score}",position=(-0.65,0.4),origin=(0,0),scale=2,color=color.yellow,background=True) 

app.run()
