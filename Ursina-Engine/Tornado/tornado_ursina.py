from ursina import *
import numpy as np

def update():
	global e
	for entity in e:
		entity.y+=.003
		entity.x=entity.y/k*np.sin(20*entity.y)
		entity.z=entity.y/k*np.cos(20*entity.y)

		if entity.y>1.5*np.pi:
			entity.y=0

def input(key):
	if key=="1":
		camera.position=(0,2.5, -20)
		camera.rotation_x=0
	if key=="2":
		camera.position=(0,20,0)
		camera.rotation_x=90

app=Ursina()

num=300
k=2
y=np.linspace(0, 1.5*np.pi, num)
x=y/k*np.sin(20*y)
z=y/k*np.cos(20*y)

e=[None]*num
for i in range(num):
	e[i]=Entity(model="sphere", color=color.random_color(), scale=.1, position=(x[i], y[i], z[i]))

camera.position=(0, 2.5, -20)

Text(text="3D Tornado Animation", position =(0, .4), origin=(0,0), background=True)

app.run()