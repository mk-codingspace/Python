import pygame
import random

class Rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = random.randint(5,25)
        self.rect.x = random.randint(-100,wn_width)
        self.rect.y = random.randint(-wn_height,-5)

    def update(self):
        
        if self.rect.bottom > wn_height:
            self.speedx = 3
            self.speedy = random.randint(5,25)
            self.rect.x = random.randint(-wn_width,wn_width)
            self.rect.y = random.randint(-wn_height,-5)
            
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy            

# Initialize
pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255)

# images
rain_img = pygame.image.load('images/rain.png')

# Set up window
wn_width = 700
wn_height = 500
wn = pygame.display.set_mode((wn_width,wn_height))
pygame.display.set_caption('Torrential Rain')

# sprite block
rain_group = pygame.sprite.Group()

for i in range(100):
    rain = Rain()
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
