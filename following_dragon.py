from ursina import *

def update():
    global dy   

    player.y += dy

    if abs(player.y) >=3:
        dy = -dy      
 
# Main code
app=Ursina() 
dy = 0.08

player = Entity(model='quad',scale=1,x=-4.5,texture='assets/dragon_head.png')

e= [None]*50

e[0] = Entity(model='circle',scale=0.2,color=color.green)
e[0].add_script(SmoothFollow(target=player, offset=(0.3,0,0)))

for i in range(1,50):

    e[i] = Entity(model='circle',scale=0.2,color=color.green)
    e[i].add_script(SmoothFollow(target=e[i-1], offset=(0.2,0,0)))

app.run()
