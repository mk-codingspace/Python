import pygame
import random

# Define some colors
WHITE = (255, 255, 255)
GRAY  = (141,141, 141)

# Clock
clock = pygame.time.Clock()

class Rain(pygame.sprite.Sprite):
    def __init__(self,color,x,y,radius):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.image = pygame.Surface((wn_width,wn_height))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.radius = self.radius + 1
        if self.radius > random.randint(30,80):
            self.radius = random.randint(2,6)
            self.x = random.randint(0,wn_width)
            self.y = random.randint(0,wn_height)
            
        self.image.fill(WHITE)
        pygame.draw.circle(self.image,self.color,(self.x,self.y),self.radius,1)
            
# Initialize
pygame.init()

wn_width = 700
wn_height = 500
wn = pygame.display.set_mode((wn_width,wn_height))
pygame.display.set_caption('It is a rainy day')

# sprite block
rain_group = pygame.sprite.Group()

for i in range(50):
    x = random.randint(0,wn_width)
    y = random.randint(0,wn_height)
    rain = Rain(GRAY, x, y,random.randint(2,6))
    rain_group.add(rain)

# -------- Main Program Loop -----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
# Update
    rain_group.update()

# Draw all the spites
    wn.fill(WHITE)
    rain_group.draw(wn)
    pygame.display.flip()
    clock.tick(30)
    
# quit
pygame.quit()
quit()
