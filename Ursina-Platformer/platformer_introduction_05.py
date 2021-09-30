from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

def update():
    global speed,dx,size, switch

    full_bar.x = camera.x - size//2
    green_bar.x = full_bar.x

    if switch == 1:
        dx += speed * time.dt
        if abs(dx) > 2:
            speed *= -1
            dx = 0
        for enemy in enemies:
            enemy.x += speed * time.dt

            # Collision with enemies
            if abs(player.x - enemy.x) < 1 and abs(player.y - enemy.y) < 1:
                player.rotation_z = 90
                green_bar.scale_x = 0
                switch = 0

    # Check if trapped
    dis = abs(player.x - trap.x)
    if (abs(dis-size)%size <= 1 or abs(dis-size)%size >= size-1) and \
       abs(player.y - ground.y) <=1:
        player.color = color.red

        # Check Health Bar
        green_bar.scale_x -= shrink * time.dt

        if green_bar.scale_x < 0.1:
            player.rotation_z = 90
            switch = 0
    else:
        player.color = color.white

class Health_Bar(Entity):
    def __init__(self,y,z,r,g,b):
        super().__init__()
        self.model = 'quad'
        self.scale = (10,0.5)
        self.color = color.rgb(r,g,b)
        self.y = y
        self.z = z
        self.origin=(-.5,-.5)
    

class Enemy(Entity):
    def __init__(self,x,y):
        super().__init__()
        self.model = 'cube'
        self.texture = 'assets/ghost.png'
        self.color = color.green
        self.x = x
        self.y = y

app = Ursina()

speed = 1
switch = 1
dx = 0
shrink = 2

size = 13

bg = Entity(model='quad', scale=(size,6), texture='assets/sky_cloud',z=0.5)
player = PlatformerController2d(y=1, z=-0.01, scale=(1,1),color=color.white,texture='assets/guy.png')
ground = Entity(model='quad', y=-2, scale_x=10, collider='box', color=color.yellow)
wall = Entity(model='cube', color=color.azure, scale=(1,3), x=5.5, collider='box')
level = Entity(model='quad', color=color.violet, scale=(3,1), x=2, collider='box')
ceiling = Entity(model='quad', color=color.cyan, scale=(3,1), x=-2.5, y=1,
                 collider='box')
trap = Entity(model='quad', scale=(2,1), x=-6, y=-2, texture='assets/trap.png', collider='box')

# Health Bar

full_bar = Health_Bar(4,0, 255,0,0)
green_bar = Health_Bar(4,-0.01,0,255,0)

enemies = []

enemy = Enemy(2-1,1)
enemies.append(enemy)

enemy = Enemy(-2.5-1,2)
enemies.append(enemy)

# Duplicate loop
extension = 1
for m in range(extension):
    duplicate(bg, x=size*(m+1))
    duplicate(bg, x=-size*(m+1))
    
    duplicate(ground, x=size*(m+1))
    duplicate(ground, x=-size*(m+1))
    
    duplicate(wall, x=5.5+size*(m+1))
    duplicate(wall, x=5.5-size*(m+1))
    
    duplicate(level, x=2+size*(m+1))
    duplicate(level, x=2-size*(m+1))

    duplicate(ceiling, x=-2.5+size*(m+1))
    duplicate(ceiling, x=-2.5-size*(m+1))

    duplicate(trap, x=-6+size*(m+1))
    duplicate(trap, x=-6-size*(m+1))

    enemy = Enemy(2-1+size*(m+1),1)
    enemies.append(enemy)
    enemy = Enemy(2-1-size*(m+1),1)
    enemies.append(enemy)

    
    enemy = Enemy(-2.5-1+size*(m+1),2)
    enemies.append(enemy)
    enemy = Enemy(-2.5-1-size*(m+1),2)
    enemies.append(enemy)

# Camera
camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

app.run()
 
