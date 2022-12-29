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
        self.collision_sprites = pygame.sprite.Group()
        self.pipe_sprites = pygame.sprite.Group()

        # sprite setup
        Background(self.all_sprites)
        Ground([self.all_sprites, self.collision_sprites])
        self.bird = Bird(self.all_sprites)

        # timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

        # text
        self.font = pygame.font.Font('graphics/font/BD_Cartoon_Shout.ttf', 30)
        self.score = 0
        self.passing_pipe = False

    def display_score(self):
        score_surface = self.font.render(str(int(self.score)), True, 'black')
        score_rect = score_surface.get_rect(midtop = (WIDTH/2, HEIGHT/30))
        self.screen.blit(score_surface, score_rect)

    def collisions(self):
        if pygame.sprite.spritecollide(self.bird, self.collision_sprites, False, pygame.sprite.collide_mask)\
             or self.bird.rect.bottom <= -100:
            print('collision')
            pygame.quit()
            sys.exit()

    def run(self):
        last_time = time.time()

        while True:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            if len(self.pipe_sprites) > 0:
                if self.bird.rect.right < self.pipe_sprites.sprites()[0].rect.right and self.passing_pipe == False:
                    self.passing_pipe = True
                    
                if self.passing_pipe == True and self.bird.rect.left > self.pipe_sprites.sprites()[0].rect.right:
                    self.score += 1 
                    self.passing_pipe = False

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.obstacle_timer:
                    pipe_height = random.randint(200, 400)
                    Obsticle("down", pipe_height, [self.all_sprites, self.collision_sprites, self.pipe_sprites])
                    Obsticle("up", pipe_height, [self.all_sprites, self.collision_sprites, self.pipe_sprites])

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.bird.jump()

            # game logic
            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.screen)
            self.display_score()

            pygame.display.update()
            self.clock.tick(FRAMERATE)
