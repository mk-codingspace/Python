from ursina import *
from datetime import datetime
import math

def update():
    global text
    t = datetime.now()
    hour, minute, second = t.hour , t.minute, t.second

    # Digital clock
    text.y = 1
    text=Text(f"{str(hour).zfill(2)} : {str(minute).zfill(2)} : {str(second).zfill(2)}",
              position=(0,.4), origin=(0,0),scale=2, background=True)

    # hour hand
    hour *= 30 # 30 degrees per hour
    angle = hour*math.pi/180 
    hr.x = hr_radius/2 * math.cos(90*(math.pi/180) - angle)
    hr.y = hr_radius/2 * math.sin(90*(math.pi/180) - angle)
    hr.rotation_z = hour

    # minutes hand
    minute *= 6 # 6 degrees per minute
    angle = minute*math.pi/180 
    mn.x = mn_radius/2 * math.cos(90*(math.pi/180) - angle)
    mn.y = mn_radius/2 * math.sin(90*(math.pi/180) - angle)
    mn.rotation_z = minute
    
    # second hand
    second *= 6 # 6 degrees per second
    angle = second*math.pi/180 
    sd.x = sd_radius/2 * math.cos(90*(math.pi/180) - angle)
    sd.y = sd_radius/2 * math.sin(90*(math.pi/180) - angle)
    sd.rotation_z = second     

# draw dots
def draw_dots(degree):
    x = 2.3 * math.cos(90*math.pi/180 - degree*math.pi/180)
    y = 2.3 * math.sin(90*math.pi/180 - degree*math.pi/180)
    
    scale = 0.05
    if degree%30 == 0: scale = 0.15
    if degree%90 == 0: scale = 0.3

    return scale,x,y

# Main game    
app=Ursina()
wall = Entity(model='quad',scale=(15,10), texture='assets/wall.png')

text = Text(text='')
clock = Entity(model='circle',color = color.black,scale=5)

#hour, minute and second hands
hr_radius = 1.8
hr = Entity(model='quad',scale=(0.1,hr_radius),color = color.gold,
            y=hr_radius/2,z=-0.1,origin=(0,0))

mn_radius = 2.1
mn = Entity(model='quad',scale=(0.05,mn_radius),color=color.pink,
            y=mn_radius/2,z=-0.1,origin=(0,0))

sd_radius = 2.4
sd = Entity(model='quad',scale=(0.03,sd_radius),color = color.lime,
            y=sd_radius/2,z=-0.1,origin=(0,0))

# Draw dots 
for degree in range(0,360,6):
    scale,x,y=draw_dots(degree)
    Entity(model='circle',scale=scale,position=(x,y),z=-0.1)

# Put on brand Text
Text(text='MK', position=(0,0.15),origin=(0,0),scale=2,color=color.red)

app.run()

