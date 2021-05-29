from ursina import *

def input(key):
    if key == '1':
        a.state = 'faucet'
    if key == '2':
        a.state = 'faucet_running'

app=Ursina()
Entity(model='quad',texture='assets/faucet.png',position=(0,0,0),scale=5)
faucet_running = Animation('assets/running_water', position=(0.5,-2.8, 0),
                scale=(0.5,2.5,1), fps=8,loop=True, autoplay=True)

Animation('assets/anima/tentakelding', position=(3,0,0),
                       fps=50,loop=True, autoplay=True)

a = Animator(
    animations = {
     'faucet' : Entity(model='quad',texture='assets/faucet.png',position=(0,0,0),scale=5),
     'faucet_running' : faucet_running
    }
)
a.state = 'faucet'

app.run()
