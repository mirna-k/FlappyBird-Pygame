import pygame, sys, time, random
from settings import *
from sprites import Background, Ground, Bird, Obsticle

class Game():
    def __init__(self) -> None:
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        # sprite setup
        Background(self.all_sprites)
        Ground(self.all_sprites)
        self.bird = Bird(self.all_sprites)

        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)


    def run(self):
        last_time = time.time()

        while True:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.obstacle_timer:
                    pipe_height = random.randint(200, 400)
                    Obsticle("down", pipe_height, self.all_sprites)
                    Obsticle("up", pipe_height, self.all_sprites)

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.bird.jump()

            # game logic
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FRAMERATE)
