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
FONT=pygame.font.SysFont("comicsans", 30)
SCORE_INCREASE=.01
GEN=0

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
		self.dead=False
		self.score=0

	def collision(self, pipes):
		for pipe in pipes:
			if self.bird_rect.colliderect(pipe.bottom_pipe_rect) or \
			self.bird_rect.colliderect(pipe.top_pipe_rect):
				return True
		if self.bird_rect.midbottom[1]>=WN_HEIGHT or self.bird_rect.midtop[1]<0:
			return True

		return False

	def find_nearest_pipes(self, pipes):
		nearest_pipe_top=None
		nearest_pipe_bottom=None
		min_distance=WN_WIDTH
		for pipe in pipes:
			curr_distance=pipe.bottom_pipe_rect.topright[0]-self.bird_rect.topleft[0]
			if curr_distance<0:
				continue
			elif curr_distance <= min_distance:
				min_distance = curr_distance
				nearest_pipe_bottom = pipe.bottom_pipe_rect
				nearest_pipe_top = pipe.top_pipe_rect
		return nearest_pipe_top, nearest_pipe_bottom

	def get_distances(self, top_pipe, bottom_pipe):
		distance=[WN_WIDTH]*3
		distance[0]=top_pipe.centerx-self.bird_rect.centerx
		distance[1]=self.bird_rect.topleft[1]-top_pipe.bottomright[1]
		distance[2]=bottom_pipe.topright[1]-self.bird_rect.bottomright[1]

		return distance

	def draw_lines(self, top_pipe, bottom_pipe):
		pygame.draw.line(WN, RED, self.bird_rect.midright, top_pipe.midbottom, 5)
		pygame.draw.line(WN, RED, self.bird_rect.midright, bottom_pipe.midtop, 5)

#Game loop
def game_loop(genomes, config):

	global GEN
	GEN+=1
	birds=[]
	nets=[]
	ge=[]

	pipe_list=[]

	for _, genome in genomes:
		net=neat.nn.FeedForwardNetwork.create(genome, config)
		genome.fitness=0
		nets.append(net)
		birds.append(Bird())
		ge.append(genome)

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==PIPE_EVENT:
				bottom_height=random.choice(PIPE_BOTTOM_HEIGHTS)
				pipe_list.append(Pipe(bottom_height))

			

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

		alive_birds=0
		max_score=0

		#print(len(pipe_list))
		for i, bird in enumerate(birds):
			if not bird.dead:
				bird.bird_rect.centery+=GRAVITY
				bird.score+=SCORE_INCREASE

				alive_birds+=1
				max_score=max(max_score, bird.score)
				ge[i].fitness+=bird.score

				WN.blit(BIRD_IMG, bird.bird_rect)
				bird.dead=bird.collision(pipe_list)
				
				nearest_pipes=bird.find_nearest_pipes(pipe_list)
				if nearest_pipes[0]:
					distances=bird.get_distances(nearest_pipes[0], nearest_pipes[1])
					bird.draw_lines(nearest_pipes[0], nearest_pipes[1])
				else:
					distances=[WN_WIDTH]*3

				output=nets[i].activate(distances)
				max_ind=output.index(max(output))
				if max_ind==0:
					bird.bird_rect.centery-=JUMP

		if alive_birds==0:
			return

		msg=f"Gen: {GEN} Birds Alive: {alive_birds} Score: {int(max_score)}"
		text=FONT.render(msg, True, BLACK)
		WN.blit(text, (40, 20)) 
		pygame.display.update()
		CLOCK.tick(FPS)

#run game
neat_config=neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
	neat.DefaultSpeciesSet, neat.DefaultStagnation, "config.txt")
population=neat.Population(neat_config)
stats=neat.StatisticsReporter()
population.add_reporter(stats)
population.run(game_loop, 50)


