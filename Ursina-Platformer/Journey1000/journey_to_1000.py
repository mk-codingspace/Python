from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

def update():
    global m,num, text
    m += 1
    n = m%n_frame
    speed = 0.5 if n<n_frame//2 else -0.5
   
    for level in levels:
        level.x += time.dt * speed

    for bonus in bonuses:
        bonus.x += time.dt * speed
        bonus.rotation_y += time.dt * 400

        # Collision
        if abs(player.x - bonus.x) < 0.5 and abs(player.y - bonus.y) < 0.8:
            Animation('assets/flame',color=color.green, scale=1, position = (bonus.x,bonus.y+0.4),
                      fps=20,loop=False, autoplay=True)
            Audio('assets/coin_sound.wav')
            num += 100
            text.y = 1
            text=Text(text=f"{num} Subscribers",position=(0,0.4),origin=(0,0),scale=2,color=color.yellow,background=True) 
            bonuses.remove(bonus)
            destroy(bonus)
            if num >=1000:
                Text(text="Thank You for Your Support!",origin=(0,0),scale=3,color=color.yellow,background=True)                     
##
app = Ursina()
m = 0
n_frame = 400

# Entities
bg = Entity(model='quad', scale=(20,10), texture='assets/bg',z=0.5)
player = PlatformerController2d(y=-3, scale=(.4,.8,.01/2),color=color.white,
                                texture='assets/guy.png')
ground = Entity(model='quad', y=-4, scale_x=15, collider='box', color=color.orange)
wall = Entity(model='quad', color=color.azure, scale=(1,9), x=7.5, collider='box')
duplicate(wall,x=-7.5)

# Levels
xy = [[-1,0],[-5,-1.5],[5,-0.5],[-7,1.3],[3,2]]

levels = []
level = Entity(model='quad', texture='assets/pad_01.png',scale=(2,0.7),position=xy[0],
               collider = 'box')
levels.append(level)

levels.append(duplicate(level, texture='assets/pad_02.png',position=xy[1]))
levels.append(duplicate(level, texture='assets/pad_03.png',position=xy[2]))
levels.append(duplicate(level, texture='assets/pad_04.png',position=xy[3]))
levels.append(duplicate(level, texture='assets/pad_05.png',position=xy[4]))

# bonus
bonuses = []
imgs =['coin.png','corn.png','diamond.png','heart.png','star.png']

for i in range(5):    
    bonus = Entity(model='quad', texture='assets/'+imgs[i],scale=0.3,
                   x=xy[i][0]-0.5,y=xy[i][1]+1)
    bonuses.append(bonus)
    bonuses.append(duplicate(bonus,x=xy[i][0]+0.5))

# Text
num = 0
text=Text(text=f"{num} Subscribers",position=(0,0.4),origin=(0,0),scale=2,color=color.yellow,background=True) 

app.run()

