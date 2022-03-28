import random, pygame, neat

pygame.init()

CLOCK=pygame.time.Clock()
RED=(255, 0, 0)
BLACK=(0, 0, 0)
FPS=60

WN_WIDTH=400
WN_HEIGHT=500
WN=pygame.display.set_mode((WN_WIDTH, WN_HEIGHT))
pygame.display.set_caption("AI Plays Flappy Bird")

BG=pygame.image.load("assets/bird_bg.png")
BIRD_IMG=pygame.image.load("assets/bird.png")
BIRD_SIZE=(40, 26)
BIRD_IMG=pygame.transform.scale(BIRD_IMG, BIRD_SIZE)
GRAVITY=4
JUMP=30

PIPE_X0 = 400
PIPE_BOTTOM_IMG=pygame.image.load("assets/pipe.png")
PIPE_TOP_IMG=pygame.transform.flip(PIPE_BOTTOM_IMG, False, True)
PIPE_BOTTOM_HEIGHTS=[90, 122, 154, 186, 218, 250]
GAP_PIPE=150
PIPE_EVENT=pygame.USEREVENT
pygame.time.set_timer(PIPE_EVENT, 1000)

class Pipe:
	def __init__(self, height):
		bottom_midtop=(PIPE_X0, WN_HEIGHT-height)
		top_midbottom=(PIPE_X0, WN_HEIGHT-height-GAP_PIPE)
		self.bottom_pipe_rect = PIPE_BOTTOM_IMG.get_rect(midtop=bottom_midtop)
		self.top_pipe_rect=PIPE_TOP_IMG.get_rect(midbottom=top_midbottom)

	def display_pipe(self):
		WN.blit(PIPE_BOTTOM_IMG, self.bottom_pipe_rect)
		WN.blit(PIPE_TOP_IMG, self.top_pipe_rect)

class Bird:
	def __init__(self):
		self.bird_rect = BIRD_IMG.get_rect(center=(WN_WIDTH//2, WN_HEIGHT//2))


#Game loop
def game_loop():

	bird=Bird()
	pipe_list=[]

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==PIPE_EVENT:
				bottom_height=random.choice(PIPE_BOTTOM_HEIGHTS)
				pipe_list.append(Pipe(bottom_height))

			keystate=pygame.key.get_pressed()
			if keystate[pygame.K_SPACE]:
				bird.bird_rect.centery-=JUMP

		WN.blit(BG, (0,0))
		remove_pipes=[]

		for pipe in pipe_list:
			pipe.top_pipe_rect.x-=3
			pipe.bottom_pipe_rect.x-=3
			pipe.display_pipe()

			if pipe.top_pipe_rect.x<-100:
				remove_pipes.append(pipe)

		for r in remove_pipes:
			pipe_list.remove(r)

		print(len(pipe_list))
		bird.bird_rect.centery+=GRAVITY
		WN.blit(BIRD_IMG, bird.bird_rect)
		pygame.display.update()
		CLOCK.tick(FPS)

#run game
game_loop()


