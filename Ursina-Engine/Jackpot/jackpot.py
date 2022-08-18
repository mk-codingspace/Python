from ursina import *
from random import randint

def update():
    global m1,m2,m3,mm1,mm2,mm3,k1,k2,k3
    global run,run1,run2,run3
    global speed1, speed2, speed3
    
    if run:
        for i, slot in enumerate(slots_1):
            slot.y -= speed1*time.dt
            if slot.y < -3:
                m1 += 1
                slot.y = slots_1[i-2].y+1.2
                if m1 == mm1:
                    k1 = k1+ mm1
                    speed1 = 0
                    run1=True
                    
        for j, slot in enumerate(slots_2):
            slot.y -= speed2*time.dt
            if slot.y < -3:
                m2 += 1
                slot.y = slots_2[j-2].y+1.2
                if m2 == mm2:
                    k2 = k2+ mm2
                    speed2 = 0
                    run2=True

        for l, slot in enumerate(slots_3):
            slot.y -= speed3*time.dt
            if slot.y <-3:
                m3 += 1
                slot.y = slots_3[l-2].y+1.2
                if m3 == mm3:
                    k3 = k3+ mm3
                    speed3 = 0
                    run3=True
                
                    
        if run1 and run2 and run3 and (k1%3 == k2%3 == k3%3):
            money.y -= time.dt*3
        
def go():
    global m1,m2,m3,mm1,mm2,mm3
    global run,run1,run2,run3
    global speed1, speed2, speed3
    
    run = True
    run1=run2=run3=False
    m1=m2=m3=0
    speed1 = speed2 = speed3 = 2
    
    mm1 = randint(3,11)
    mm2 = randint(3,11)
    mm3 = randint(3,11)
    money.y = 10

app = Ursina()
window.color = color.rgb(128,255,128)
run = False
speed1 = speed2 = speed3 = 0
m1 = m2 = m3 = 0
k1 = k2 = k3 = 0
imgs = ['assets/coin.png','assets/diamond.png','assets/star.png']
machine = Entity(model='quad',scale=(10,8),texture='assets/jackpot.png',
              z=-0.1)
money = Entity(model='quad',scale=(10,8),texture='assets/money.png',
              z=-0.15,y=10)

slot10 = Entity(model='quad',scale=(1,1),texture=imgs[0],x=-2.5,y=1.8)
slot11 = duplicate(slot10,texture=imgs[1], y=0.6)
slot12 = duplicate(slot10,texture=imgs[2], y=-0.6)

slot20 = Entity(model='quad',scale=(1,1),texture=imgs[0],x=-0.4,y=0.6)
slot21 = duplicate(slot20,texture=imgs[1], y=-0.6)
slot22 = duplicate(slot20,texture=imgs[2], y=-1.8)

slot30 = Entity(model='quad',scale=(1,1),texture=imgs[0],x=1.7,y=-0.6)
slot31 = duplicate(slot30,texture=imgs[1], y=-1.8)
slot32 = duplicate(slot30,texture=imgs[2], y=-3)

slots_1 = [slot10,slot11,slot12]
slots_2 = [slot20,slot21,slot22]
slots_3 = [slot30,slot31,slot32]

B = Button(text='', color=color.rgba(0,0,0,0),
           icon = 'assets/button.png',scale= .2, x=.4,y=-.35)
B.on_click = go

app.run()
