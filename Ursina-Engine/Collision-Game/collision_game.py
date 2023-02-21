from ursina import *
from random import uniform

def update():
    global diamonds, coins, bombs, score, text

    basket.x += held_keys['right arrow']*time.dt*basket_dx
    basket.x -= held_keys['left arrow']*time.dt*basket_dx
    
    if basket.x >=6: basket.x = 6  
    if basket.x <=-6: basket.x = -6  
    
    for diamond in diamonds:
        diamond.y += time.dt * diamond.dy
        if diamond.y < uniform(-10,-4):
            diamond.position = (uniform(-5,5),uniform(4,10),-0.1)
        hit_diamond = basket.intersects(diamond)
        if hit_diamond.hit:
            Audio('assets/bell_sound.wav')
            diamond.position = (uniform(-5,5),uniform(4,10),-0.1)
            score += 5
            text.y = 1
            text=Text(text=f"Score: {score}",position=(-0.7,0.45),origin=(0,0),scale=2,color=color.yellow,background=True) 
        if score < 0:
            diamond.dy = 0
            Text(text='You lost! Reload the game!',origin=(0,0),scale=2,color=color.yellow,background=True)

    for coin in coins:
        coin.y += time.dt * coin.dy
        if coin.y < uniform(-10,-4):
            coin.position = (uniform(-5,5),uniform(4,10),-0.1)
        hit_coin = basket.intersects(coin)
        if hit_coin.hit:
            Audio('assets/bell_sound.wav')
            coin.position = (uniform(-5,5),uniform(4,10),-0.1)
            score += 1
            text.y = 1
            text=Text(text=f"Score: {score}",position=(-0.7,0.45),origin=(0,0),scale=2,color=color.yellow,background=True) 
        if score < 0:
            coin.dy = 0
            Text(text='You lost! Reload the game!',origin=(0,0),scale=2,color=color.yellow,background=True)

    for bomb in bombs:
        bomb.y += time.dt * bomb.dy
        if bomb.y < uniform(-10,-4):
            bomb.position = (uniform(-5,5),uniform(4,10),-0.1)
        hit_bomb = basket.intersects(bomb)
        if hit_bomb.hit:
            Audio('assets/explosion_sound.wav')
            bomb.position = (uniform(-5,5),uniform(4,10),-0.1)
            score -= 10
            text.y = 1
            text=Text(text=f"Score: {score}",position=(-0.7,0.45),origin=(0,0),scale=2,color=color.yellow,background=True) 
        if score < 0:
            bomb.dy = 0
            Text(text='You lost! Reload the game!',origin=(0,0),scale=2,color=color.yellow,background=True)
            
class Target(Entity):
    def __init__(self, img):

        super().__init__()
        self.model = 'quad'
        self.texture = img
        self.position = (uniform(-5,5),uniform(4,10),-0.1)
        self.collider = 'box'
        self.dy = uniform(-0.5,-3)
        
app = Ursina()

left_wall = Entity(model='quad',color=color.green,scale=(0.6,10),position=(-7,0,0),collider='box')
right_wall = duplicate(left_wall,x=7)
basket = Entity(model='quad',texture='assets/basket.png',position=(0,-4,-0.1),collider='box')
basket_dx = 5
score = 0
text=Text(text=f"Score: {score}",position=(-0.7,0.45),origin=(0,0),scale=2,color=color.yellow,background=True)

diamonds = []
coins = []
bombs = []
for i in range(3):
    diamond = Target('assets/diamond.png')
    diamonds.append(diamond)

    coin = Target('assets/coin.png')
    coins.append(coin)

for i in range(6):
    bomb = Target('assets/bomb.png')
    bombs.append(bomb)
    
app.run()