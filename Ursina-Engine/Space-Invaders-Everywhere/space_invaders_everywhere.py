from ursina import *
import math
from random import randint

def update():
    global bullets,fireballs, score, text
    player.rotation_z += held_keys['right arrow'] * player.d_angle
    player.rotation_z -= held_keys['left arrow']  * player.d_angle

    for fireball in fireballs:

        fireball.x += fireball.dx
        fireball.y += fireball.dy

        if sqrt(fireball.x **2 + fireball.y ** 2) < 0.7:
            Entity(model='quad', scale=60, color=color.gray)
            player.z = 10
            Text(text='You lost! Reload the game!',origin=(0,0),scale=2,color=color.yellow,background=True)


    for bullet in bullets:
        bullet.x += time.dt*bullet.dx
        bullet.y += time.dt*bullet.dy
        
        hit_info = bullet.intersects()
        if hit_info.hit:
            Animation('assets/explosion', position=hit_info.entity.position,
                scale=1, fps=10,loop=False, autoplay=True)
            Audio('assets/explosion_sound.wav')
            bullet.z = 1

            score += 1
            text.z = 1
            text=Text(text=f"Score: {score}",position=(-0.65,0.4),origin=(0,0),scale=2,color=color.yellow,background=True) 

            if hit_info.entity in fireballs:
                hit_info.entity.angle = randint(0,359)
                hit_info.entity.scale = randint(40,80)/100
                hit_info.entity.speed = randint(6,12)/1000
                hit_info.entity.distance = randint(5,10)

                hit_info.entity.position = \
                        (hit_info.entity.distance*math.cos(hit_info.entity.angle/180*math.pi),
                         hit_info.entity.distance*math.sin(hit_info.entity.angle/180*math.pi))
                hit_info.entity.dx = -math.cos(hit_info.entity.angle/180*math.pi)*hit_info.entity.speed
                hit_info.entity.dy = -math.sin(hit_info.entity.angle/180*math.pi)*hit_info.entity.speed


def input(key):
    global bullets
    if key == "space":
        Audio('assets/laser_sound.wav')
        bullet = Bullet()
        bullets.append(bullet)

class Fireball(Entity):
    def __init__(self,angle):

        super().__init__()
        self.model='quad'
        self.texture = 'assets/fireball.png'
        self.angle = angle
        self.scale = randint(40,80)/100
        self.distance = 5

        self.position = (self.distance*math.cos(self.angle/180*math.pi),
                         self.distance*math.sin(self.angle/180*math.pi))
        self.z = -0.1
        self.speed = randint(6,12)/1000
        self.dx = -math.cos(self.angle/180*math.pi)*self.speed
        self.dy = -math.sin(self.angle/180*math.pi)*self.speed
        self.collider = 'box'
      
class Player(Entity):
    def __init__(self):

        super().__init__()
        self.parent = camera.ui
        self.model='quad'
        self.scale = (0.3,0.2)
        self.texture='assets/gun.png'
        self.position = (0,0)
        self.d_angle = 1

class Bullet(Entity):
    def __init__(self):

        super().__init__()
        self.model='cube'
        self.color = color.green
        self.scale = (0.12,0.5,1)
        self.position = player.position
        self.z = 0
        self.rotation_z = player.rotation_z
        self.dx = 5 * math.sin(player.rotation_z/180*math.pi)
        self.dy = 5 * math.cos(player.rotation_z/180*math.pi)
        self.collider = 'box'
        
            
app=Ursina()

num = 8
Entity(model='quad', scale=(20,10), texture='assets/blue_sky')
bullets = []
player = Player()
fireballs = []
for i in range(num):
    fireball = Fireball(randint(0,359))
    fireballs.append(fireball)
score = 0
text=Text(text='')
app.run()
