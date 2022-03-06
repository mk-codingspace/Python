import pygame, pymunk, math
from random import randint

class Ball():
	def __init__(self, x, y, size):
		self.size=size
		mass=self.size**2
		self.color=(randint(0, 255), randint(0, 255), randint(0, 255))
		angle=randint(0, 359)
		coeff=40000/mass
		self.body=pymunk.Body(mass)
		self.body.position=(x, y)
		self.body.velocity=(coeff*math.cos(angle*math.pi/180), coeff*math.sin(angle*math.pi/180))
		self.shape=pymunk.Circle(self.body, self.size)
		self.shape.elasticity=1
		self.shape.density=1
		space.add(self.body, self.shape)

	def draw(self):
		x=int(self.body.position.x)
		y=int(self.body.position.y)
		pygame.draw.circle(wn, self.color, (x,y), self.size)

def create_segment(pos1, pos2):
	segment_body = pymunk.Body(body_type = pymunk.Body.STATIC)
	segment_shape=pymunk.Segment(segment_body, pos1, pos2, 10)
	segment_shape.elasticity=1
	space.add(segment_body, segment_shape)

pygame.init()
wn=pygame.display.set_mode((600, 600))
clock=pygame.time.Clock()
space=pymunk.Space()

FPS=50
WHITE = (255, 255, 255)
BLACK = (0,0,0)
balls=[Ball(randint(0, 600), randint(0, 600), randint(10, 20)) for i in range(50)]
pos_tl=(0,0)
pos_tr=(600, 0)
pos_bl=(0, 600)
pos_br=(600, 600)
segment1=create_segment(pos_tl, pos_tr)
segment2=create_segment(pos_tr, pos_br)
segment3=create_segment(pos_br, pos_bl)
segment4=create_segment(pos_bl, pos_tl)

running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	wn.fill(WHITE)
	[ball.draw() for ball in balls]
	pygame.draw.line(wn, BLACK, pos_tl, pos_tr, 10)
	pygame.draw.line(wn, BLACK, pos_tr, pos_br, 10)
	pygame.draw.line(wn, BLACK, pos_br, pos_bl, 10)
	pygame.draw.line(wn, BLACK, pos_bl, pos_tl, 10)

	pygame.display.flip()
	clock.tick(FPS)
	space.step(1/FPS)

pygame.quit()