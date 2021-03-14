from ursina import *

def update():
    global score,m,offset
    m = m + 1
    if m % 60 == 0 and score > -1:
        print_on_screen(f"Countdown: {score}",position=(-0.8,.45), scale=2, duration=1)
        score = score - 1

    if score < 0:
        offset = offset + time.dt * 0.3 # Add a small number to this variable
        cube2.texture='img/rocket.png'
        cube2.y = 0
        setattr(cube, "texture_offset", (0, offset))  # Assign as a texture offset

  
app=Ursina()
score = 10
m = 0
offset = 0

cube = Entity(model='cube', scale=(3.5,5.5,3.5), texture="img/starbg.png")
cube2 = Entity(model='cube', color=color.rgba(255,255,255,255), scale=(3.6,5,3.6),
               texture="img/rocket_0.png",y=-0.9)

app.run()
