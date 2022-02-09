from ursina import *

def add_item():
	global m
	x=m%3-1
	y=(m%15-6)//3
	if m//15>3:
		m=15*3
	field.z=-.11* (m//15)

	E= Entity(model="quad", texture="assets/" + imgs[m//15], position=(x, y, -.1-.1*(m//15)))
	
	for i in range(len(texts)):
		if i==m//15:
			texts[i].scale=2
			texts[i].color=color.gold
		else:
			texts[i].scale=1
			texts[i].color=color.white

	m+=1

app=Ursina()

window.color=color.rgb(128, 255, 128)
m=0
imgs=["cookie.png", "coin.png", "bill.png", "house.png"]
field = Entity(model="quad", scale=(3, 5), texture="assets/grid.png")

texts=[]
texts.append(Text(text="Student", x=.4, y=-.12, background=True))
texts.append(Text(text="Employed", x=.4, y=-.04, background=True))
texts.append(Text(text="Middle Class", x=.4, y=.04, background=True))
texts.append(Text(text="Rich", x=.4, y=.12, background=True))

B = Button(text="+", color=color.azure, scale=.125, x=-.5)
B.on_click = add_item

app.run()
