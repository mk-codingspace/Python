from ursina import *
import numpy as np

app=Ursina()


def update():
	global angle
	angle-=.5
	camera.rotation_z=angle

a=1
num=60
theta=np.linspace(0, 3*np.pi, num)

b=.2
x1=a*np.cos(theta)*np.exp(b*theta)
y1=a*np.sin(theta)*np.exp(b*theta)
e1=[None]*num

x2=-a*np.cos(theta)*np.exp(b*theta)
y2=-a*np.sin(theta)*np.exp(b*theta)
e2=[None]*num

b=.25

x3=a*np.cos(theta)*np.exp(b*theta)
y3=a*np.sin(theta)*np.exp(b*theta)
e3=[None]*num

x4=-a*np.cos(theta)*np.exp(b*theta)
y4=-a*np.sin(theta)*np.exp(b*theta)
e4=[None]*num

for i in range(num):
	e1[i]=Entity(model="sphere", color=color.red, scale=.1, position=(x1[i], y1[i]))
	e2[i]=Entity(model="sphere", color=color.green, scale=.1, position=(x2[i], y2[i]))
	e3[i]=Entity(model="sphere", color=color.yellow, scale=.1, position=(x3[i], y3[i]))
	e4[i]=Entity(model="sphere", color=color.cyan, scale=.1, position=(x4[i], y4[i]))

Entity(model="sphere", scale=(2, .6, 1), color=color.rgb(255, 255, 204))
angle=0

app.run()
