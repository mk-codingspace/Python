import pygame, pymunk 

def NewBall(space,pos):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,10)
    shape.elasticity = 1
    space.add(body,shape)
    return shape

# define constants  
WIDTH = 600  
HEIGHT = 500  
FPS = 80  

# define colors  
BLACK = (0 , 0 , 0)  
GREEN = (128 , 255 , 128)
RED = (255,0,0)

# initialize pygame and create window 
pygame.init()  
wn = pygame.display.set_mode((WIDTH , HEIGHT))  
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0,200)
       
static_ball_body = pymunk.Body(body_type = pymunk.Body.STATIC)
static_ball_body.position = (300,300)
static_ball_shape = pymunk.Circle(static_ball_body,30)
static_ball_shape.elasticity = 0.9
space.add(static_ball_body,static_ball_shape)

segment_body = pymunk.Body(body_type = pymunk.Body.STATIC)
segment_shape = pymunk.Segment(segment_body,(0,350),(600,400),5)
segment_shape.elasticity = 0.9
space.add(segment_body,segment_shape)

balls = []

running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(NewBall(space,event.pos))

    wn.fill(GREEN)
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(wn,RED,(pos_x,pos_y),10)

    pygame.draw.circle(wn,BLACK, static_ball_body.position, 30)
    pygame.draw.line(wn,BLACK,(0,350),(600,400),5)
    
    pygame.display.flip()
    clock.tick(FPS)
    space.step(1/FPS)

pygame.quit()


