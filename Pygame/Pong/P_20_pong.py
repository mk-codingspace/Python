# Import modules
import pygame
import time

# Initiate pygame. Always needed
pygame.init() 

# Clock
clock = pygame.time.Clock()

# color
BLACK = (0,0,0)
GREEN = (144,238,144)
RED = (255,0,0)
WHITE = (255,255,255)

# window with size
wnWidth = 600
wnHeight = 500
wn = pygame.display.set_mode((wnWidth,wnHeight))
pygame.display.set_caption('Pong')

# Central line
startX=wnWidth//2; startY=0;
endX=wnWidth//2; endY=wnHeight;
lineWidth=5

# Paddle
pWidth = 20
pLength = 100

# Sounds
pong_sound=pygame.mixer.Sound('assets/pong_sound.wav')
whistle = pygame.mixer.Sound('assets/whistle.wav')

class Ball:
    def __init__(self,x,y,radius):
        self.x = x # x, y is the center coordinate 
        self.y = y
        self.radius = radius
        self.speedx = 4
        self.speedy = -3
        self.scoreA = 0
        self.scoreB = 0

    def update(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
        
        # boundary checking, top and bottom
        if self.y - self.radius < 0 or \
           self.y + self.radius > wnHeight:
               self.speedy = -self.speedy
               
        # boundary checking, left and right
        if self.x + self.radius < 0:
            self.x = wnWidth//2
            self.y = wnHeight//2
            whistle.play()
            self.scoreB = self.scoreB + 1
            
        if self.x - self.radius > wnWidth:
            whistle.play()
            self.x = wnWidth//2
            self.y = wnHeight//2
            self.scoreA = self.scoreA + 1           

    def draw(self,wn):
       pygame.draw.circle(wn,RED,(self.x,self.y),self.radius)

class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speedy = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if self.x == 0: # Left paddle
            if keystate[pygame.K_w]:
                self.speedy = -5
            elif keystate[pygame.K_s]:
                self.speedy = 5
            else:
                self.speedy = 0
        else:  # Right Paddle
            if keystate[pygame.K_UP]:
                self.speedy = -5
            elif keystate[pygame.K_DOWN]:
                self.speedy = 5
            else:
                self.speedy = 0            
        self.y = self.y + self.speedy

    def draw(self,wn):
        pygame.draw.rect(wn, BLACK, [self.x, self.y, self.width, self.height])       

# Functions
def scoreBoardA(score):
    font = pygame.font.Font(None,50)
    text = font.render(str(score),True,BLACK)
    textWidth = text.get_width()
    x = int(wnWidth//2-textWidth//2 - 50)
    wn.blit(text,(x,20)) 

def scoreBoardB(score):
    font = pygame.font.Font(None,50)
    text = font.render(str(score),True,BLACK)
    textWidth = text.get_width()
    x = int(wnWidth//2-textWidth//2 + 50)
    wn.blit(text,(x,20))

# Create objects
radius = 15
ball = Ball(wnWidth//2,wnHeight//2, radius)
playerA = Player(0,wnHeight//2-pLength/2,pWidth,pLength)
playerB = Player(wnWidth-pWidth,wnHeight//2-pLength//2,pWidth,pLength)

# Game loop
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

    playerA.update()
    playerB.update()

    ball.update()

    wn.fill(GREEN)
    pygame.draw.line(wn, WHITE, (startX, startY), (endX, endY),lineWidth)

    playerA.draw(wn)
    playerB.draw(wn)
    ball.draw(wn)

    # Collision right
    if ball.x + ball.radius > playerB.x and \
       ball.x + ball.radius < playerB.x + playerB.width:
        if ball.y + ball.radius > playerB.y and \
           ball.y - ball.radius < playerB.y + playerB.height:
            pong_sound.play()
            ball.speedx = -ball.speedx
    
    # Collision left
    if ball.x - ball.radius < playerA.x + playerA.width and \
       ball.x - ball.radius > 0:
        if ball.y + ball.radius > playerA.y and \
           ball.y - ball.radius < playerA.y + playerA.height:
            pong_sound.play()
            ball.speedx = -ball.speedx

    scoreBoardA(ball.scoreA)
    scoreBoardB(ball.scoreB)
    
    pygame.display.update()
    clock.tick(30) 

# quit
pygame.quit() 
quit()
