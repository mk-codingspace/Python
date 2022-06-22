from ursina import *
import random

def update():
	global offset, collision
	offset+=time.dt * .3
	setattr(track, "texture_offset", (0, offset))

	car0.x+=held_keys['d']*time.dt*.2
	car0.x-=held_keys['a']*time.dt*.2

	if car0.x>=.24:
		car0.x=.24
	if car0.x<=-.28:
		car0.x=-.28

	for car in cars:
		#for car1 and car2
		if car.rotation_y==0:
			car.z-=time.dt*random.uniform(.02, .05)
		else: #for car3 and car4
			car.z-=time.dt*random.uniform(.09, .12)

		#bottom boundary checking
		if car.z<-.3:
			car.z=.4

		if abs(car0.x-car.x)<.05:
			if abs(car0.z-car.z)<.05:
				collision=True

	if collision:
		car0.rotation_y+=time.dt*100
		if car0.rotation_y>=360:
			collision=False
			car0.rotation_y=0

class Car(Entity):
	scale_y=.0001
	scale_z=.06
	def __init__(self, img, scale_x, position, angle):
		super().__init__()
		self.parent=track
		self.model="cube"
		self.texture=img
		self.scale=(scale_x, self.scale_y,self.scale_z)
		self.position=position
		self.collider="box"
		self.rotation_y=angle

app=Ursina()
window.color=color.orange
offset=0
collision=False

cars_img=["assets/car0.png", "assets/car1.png", "assets/car2.png", "assets/car3.png", "assets/car4.png"]
track=Entity(model='cube', color=color.green, scale=(10, .5, 60), position=(0,0), texture="assets/track.png")

car0=Car(cars_img[0], 0.15, (.05, 1, -.12), 0)
car1=Car(cars_img[1], 0.08, (.05, 1, .2), 0)
car2=Car(cars_img[2], 0.07, (.19, 1, .1), 0)
car3=Car(cars_img[3], 0.07, (-.09, 1, 0), 180)
car4=Car(cars_img[4], 0.07, (-.23, 1, -.1), 180)

cars=[car1, car2, car3, car4]

camera.position=(0,8, -26)
camera.rotation_x=20

app.run()
