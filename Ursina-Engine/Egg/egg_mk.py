from ursina import *
import random

def update():
    global run,t
    
    if run:
        bar_1.scale_y +=0.5 * time.dt
        bar_1.scale_y = clamp(bar_1.scale_y,0,maxscale)        
        bar_2.scale_y -=0.5 * time.dt
        
    if held_keys['space'] or bar_1.scale_y >= maxscale:
        run = False
        
    if run == False:
        t += 30*time.dt
        t = clamp(t,0,90)
        angle = t*(math.pi/180)
        bar_1.origin = Vec3(0,0,0)
        s1 = bar_1.scale_y/2
        bar_1.x = s1 * math.cos(90*(math.pi/180) - angle)-3
        bar_1.y = s1 * math.sin((90*math.pi/180) - angle)-2.9
        bar_1.rotation_z = t

        bar_2.origin = Vec3(0,0,0)
        s2 = 6-bar_2.scale_y/2 - 0.1
        bar_2.x = s2 * math.cos(90*(math.pi/180) - angle)-3
        bar_2.y = s2 * math.sin((90*math.pi/180) - angle)-2.9
        bar_2.rotation_z = t

        # Colission
        if t >= 90:

            if bar_1.scale_y >= maxscale:
                if egg.x-egg.scale_x/2 > -3 + maxscale:
                    NotBreak()
                else:
                    EggBreak()

            else:
                if egg.x-egg.scale_x/2 > -3+bar_1.scale_y and \
                   egg.x + egg.scale_x/2 < bar_2.x - bar_2.scale_y/2:
                    NotBreak()
                else:
                    EggBreak()
            
def NotBreak():
    emoji = Entity(model='quad',texture = 'assets/happy.png')
    emoji.animate_z(-2,duration = 1, loop = False)
    invoke(Func(emoji.fade_out,duration=1))
    reset()

def EggBreak():
    emoji = Entity(model='quad',texture = 'assets/angry.png')
    egg.texture='assets/broken_egg.png'
    emoji.animate_z(-2,duration = 1, loop = False)
    invoke(Func(emoji.fade_out,duration=1))
    Text(text='You lost, game Over!',position=(0,0.2),origin=(0,0),background=True)
            
def reset():
    global run,t
    t = 0
    run = True
    egg.x = random.uniform(-2,3)
    egg.texture = 'assets/egg.png'
    
    bar_1.x = -3
    bar_1.origin = (-0.5,-0.5)
    bar_1.scale_y = 0
    bar_1.rotation_z = 0

    bar_2.x = -3
    bar_2.y = 3
    bar_2.origin = (-0.5,0.5)
    bar_2.scale_y = maxscale-bar_1.scale_y
    bar_2.rotation_z = 0
    
# Main game    
app=Ursina()

t = 0
run = True
maxscale = 4.5

field = Entity(model='quad',color=color.violet,scale=(15,6))
bar_1 = Entity(model='quad',color=color.green,scale=(0.2,0),
              origin=(-0.5, -0.5), position = (-3,-2.9,-0.1),
               z=-0.1)
bar_2 = duplicate(bar_1,y=3,origin=(-0.5,0.5),
                scale_y = maxscale-bar_1.scale_y)
egg = Entity(model='quad',texture='assets/egg.png', scale=(0.8,1),
             position=(random.uniform(-2,3),-2.4,-0.1))
emoji = Entity(model='quad',z=0.1)

app.run()
