from ursina import * # Import the ursina engine


def update():
    global origin,x,speed
    for entity in circles:
        entity.z = entity.z - time.dt * 20          # Rotate all the cubes every time update is called
        if entity.z < -15:
            entity.z = origin

    x = x + time.dt * speed
    if abs(x) > 1:
        speed = speed * (-1)
    camera.position=(x,0,-20)
    
    
#--------------
app = Ursina() # Initialize the app
window.color = color.black

circles= [None]*10

circles[0] = Entity(model="cube",texture='img/ring.png',scale=3)

for i in range(1,10):
    circles[i] = Entity(model="cube",texture='img/ring.png',scale=3)
    circles[i].z = circles[i-1].z + 10

origin = circles[9].z

x=0
speed = 0.2
          
app.run() # Run the app
