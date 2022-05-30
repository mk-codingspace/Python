import pygame, random, neat

pygame.init()

# Global Constants
CLOCK = pygame.time.Clock()
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
FPS = 30
FONT = pygame.font.SysFont('comicsans', 30)

HEIGHT = 450
WIDTH = 1000
WN = pygame.display.set_mode((WIDTH, HEIGHT))

RUN_IMG = [pygame.image.load("assets/DinoRun1.png"),
           pygame.image.load("assets/DinoRun2.png")]
JUMP_IMG = pygame.image.load("assets/DinoJump.png")
SM_CACTUS = [pygame.image.load("assets/SmallCactus1.png"),
                pygame.image.load("assets/SmallCactus2.png"),
                pygame.image.load("assets/SmallCactus3.png")]
LG_CACTUS = [pygame.image.load("assets/LargeCactus1.png"),
                pygame.image.load("assets/LargeCactus2.png"),
                pygame.image.load("assets/LargeCactus3.png")]
GROUND = pygame.image.load("assets/ground.png")
CLOUD = pygame.image.load("assets/cloud.png")

class Dinosaur:
    X_POS = 80
    Y_POS = 260
    JUMP_VEL = 8.5
    GRAVITY = 0.8

    def __init__(self):
        self.img = RUN_IMG[0]
        self.run = True
        self.jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, self.img.get_width(), self.img.get_height())
        self.step_index = 0

    def move(self):
        if self.run:
            self.img = RUN_IMG[self.step_index // 4]
            self.rect.x = self.X_POS
            self.rect.y = self.Y_POS
            self.step_index += 1

        if self.jump:
            self.img = JUMP_IMG
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= self.GRAVITY
            if self.jump_vel <= -self.JUMP_VEL:
                self.jump = False
                self.run = True
                self.jump_vel = self.JUMP_VEL

        if self.step_index >= 8:
            self.step_index = 0

    def draw(self,WN,obstacles):
        WN.blit(self.img, (self.rect.x, self.rect.y))
        for obstacle in obstacles:
            pygame.draw.line(WN, GREEN, (self.rect.x + 54, self.rect.y + 11), obstacle.rect.center, 2)

class LargeCactus:
    def __init__(self,img):
        self.img = img
        self.type = random.randint(0,2)
        self.rect = self.img[self.type].get_rect()
        self.rect.x = WIDTH
        self.rect.y = 250

    def draw(self,WN):
        WN.blit(self.img[self.type],self.rect)

class SmallCactus(LargeCactus):
    def __init__(self,img):
        self.type = random.randint(0,2)
        super().__init__(img)
        self.rect.y = 275

def game_loop(genomes, config):
    obstacles = []
    dinosaurs = []
    ge = []
    nets = []

    ground_x = 0
    ground_y = 330
    cloud_x = WIDTH
    cloud_y = 150

    move_speed = 20
    score = 0

    for _, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        WN.fill(WHITE)

        # Ground
        ground_x -= move_speed
        if ground_x <= -GROUND.get_width():
            ground_x = 0
        WN.blit(GROUND, (ground_x,ground_y))
        WN.blit(GROUND, (ground_x+GROUND.get_rect().width,ground_y))

        # Cloud
        cloud_x -= move_speed/2
        if cloud_x < -100:
            cloud_x = WIDTH
        WN.blit(CLOUD, (cloud_x,cloud_y))

        # Dinosaurs
        for dinosaur in dinosaurs:
            dinosaur.move()
            dinosaur.draw(WN,obstacles)
        if len(dinosaurs) == 0:
            return

        # Obstacles
        if len(obstacles) == 0:
            if random.choice(['S','L']) == 'S':
                obstacles.append(SmallCactus(SM_CACTUS))
            else:
                obstacles.append(LargeCactus(LG_CACTUS))                
        for obstacle in obstacles:
            obstacle.draw(WN)
            obstacle.rect.x -= move_speed
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles.pop()
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    dinosaurs.pop(i)
                    ge.pop(i)
                    nets.pop(i)
                    
        # activation
        for i, dinosaur in enumerate(dinosaurs):
            output = nets[i].activate((dinosaur.rect.y,obstacle.rect.x - dinosaur.rect.x))
            if output[0] > 0.5 and dinosaur.rect.y == dinosaur.Y_POS:
                dinosaur.jump = True
                dinosaur.run = False

        # stats
        text_1 = FONT.render(f'Dinosaurs Alive:  {str(len(dinosaurs))}', True, BLACK)
        text_2 = FONT.render(f'Generation:  {population.generation+1}', True, BLACK)
        text_3 = FONT.render(f'Game Speed:  {str(move_speed)}', True, BLACK)
        WN.blit(text_1, (600, 50))
        WN.blit(text_2, (600, 80))
        WN.blit(text_3, (600, 110))
        
        # score
        score += 1
        if score % 100 == 0:
            move_speed += 1
        text = FONT.render(f'Score:  {str(score)}', True, BLACK)
        WN.blit(text, (600, 20))

        CLOCK.tick(FPS)
        pygame.display.update()
        
# Run game
neat_config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, "config.txt")
population = neat.Population(neat_config)
stats = neat.StatisticsReporter()
population.add_reporter(stats)
population.run(game_loop,50) # 50 is the maximum no of generation allowed for the AI game
