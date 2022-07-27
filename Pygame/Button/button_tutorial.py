import pygame
from random import uniform, randint

class Button:
	def __init__(self, x, y):
		self.img=B_img
		self.rect=self.img.get_rect()
		self.rect.topleft=(x,y)
		self.clicked=False

	def draw(self):
		pos=pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				self.clicked=True
				draw_circle()
			if not pygame.mouse.get_pressed()[0]:
				self.clicked=False

		WN.blit(self.img, (self.rect.x, self.rect.y))

def draw_circle():
	pos_x=uniform(100, 900)
	pos_y=uniform(100, 500)
	color=(randint(0, 255), randint(0, 255), randint(0, 255))
	pygame.draw.circle(WN, color, (pos_x, pos_y), uniform(10, 50))

pygame.init()

CLOCK=pygame.time.Clock()
FPS=30
WHITE=(255, 255, 255)
WIDTH=1000
HEIGHT=600
WN=pygame.display.set_mode((WIDTH, HEIGHT))

B_img=pygame.image.load("assets/button.png")
B_img=pygame.transform.scale(B_img, (100, 100))

B=Button(800, 400)
run=True
WN.fill(WHITE)

while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	B.draw()
	pygame.display.flip()
	CLOCK.tick(FPS)

pygame.quit()