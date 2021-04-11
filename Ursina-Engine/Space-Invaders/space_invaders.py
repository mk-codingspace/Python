from ursina import *
from random import randint

def update():
    global invaders, bullets,score,text
    player.x += held_keys['right arrow'] * time.dt * player.dx
    player.x -= held_keys['left arrow'] * time.dt * player.dx

    for invader in invaders:
        invader.y += time.dt*invader.dy

        if invader.y < -0.55:
            Entity(model='quad', scale=60, color=color.gray)
            player.y = 10
            Text(text='You lost! Reload the game!',origin=(0,0),scale=2,color=color.yellow,background=True)
            
    for bullet in bullets:
        bullet.y += time.dt*bullet.dy
        hit_info = bullet.intersects()
        if hit_info.hit:
            Audio('assets/explosion_sound.wav')
            bullet.x = 10
            score += 1
            text.y = 10
            text=Text(text=f"Score: {score}",position=(-0.65,0.4),origin=(0,0),scale=2,color=color.yellow,background=True) 

            if hit_info.entity in invaders:
                hit_info.entity.x = randint(-50,50)*0.01 
                hit_info.entity.y = randint(80,120)*0.01 


def input(key):
    global bullets
    if key == "space":
        Audio('assets/laser_sound.wav')
        bullet = Bullet()
        bullets.append(bullet)
        
class Invader(Entity):
    def __init__(self):

        super().__init__()
        self.parent = field
        self.model='quad'
        self.texture='alien.png'
        self.scale = 0.1
        self.position = (randint(-50,50)*0.01,randint(80,120)*0.01,-0.1)
        self.collider = 'box'
        self.dy = -0.15

class Player(Entity):
    def __init__(self):

        super().__init__()
        self.parent = field
        self.model='cube'
        self.color = color.orange
        self.scale = (0.1,0.2,0.2)
        self.position = (0,-0.5,-0.1)
        self.dx = 0.5

class Bullet(Entity):
    def __init__(self):

        super().__init__()
        self.parent = field
        self.model='cube'
        self.color = color.green
        self.texture = 'assets/laser'
        self.scale = (0.02,0.1,0.1)
        self.position = player.position
        self.y = player.y + 0.2
        self.collider = 'box'
        self.dy = 0.8
            
app=Ursina()

field_size = 19
Entity(model='quad', scale=60, texture='assets/blue_sky')
field=Entity(model='quad',color=color.rgba(255,255,255,0),scale=(12,18),
       position=(field_size // 2, field_size // 2, -0.01))

bullets = []
invaders = []

player = Player()
for i in range(10):
    invader = Invader()
    invaders.append(invader)
    
score = 0
text=Text(text='')

camera.position = (field_size // 2, -18, -18)
camera.rotation_x = -56

app.run()


