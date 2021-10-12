from ursina import *

def update():
    bullet.x += time.dt * 2

def consequence(balls):
    Animation('assets/explosion',
            position=(balls.x,balls.y),
            scale=(2,2),
            fps=20,
            loop=False,
            autoplay=True)
    destroy(balls)

app = Ursina()

bg = Entity(model='quad', texture='assets/sky_cloud.png',scale=(20,8),z=1)
bullet = Entity(model='quad', texture='assets/bullet.png', scale=(0.6,1),x=-8)

balls =[None]*6
for i in range(6):

    balls[i] = Trigger(trigger_targets=(bullet,),
                model='circle',
                x=-4+i*2,
                color=color.red)

    balls[i].on_trigger_enter = Func(consequence,balls[i])

app.run()
