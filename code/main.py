import pygame
import random
from settings import * 

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

# COLORS
light_blue = (173, 216, 230)
black = (5, 5, 5)
red = (227, 66, 52)

passage_width = 230
passage_height = random.randint(285, 500)

# PLAYER
player_image = pygame.image.load("graphics/bird/flying/frame-1.png").convert_alpha()
PLAYER = player_image.get_rect(center = (WIDTH/4, HEIGHT/2))

# OBSTACLES
down_obst_image = pygame.image.load("graphics/obstacles/down_pipe.png")
down_obst = down_obst_image.get_rect(topleft = (WIDTH, passage_height + passage_width/2))
up_obst_image = pygame.image.load("graphics/obstacles/up_pipe.png")
up_obst = up_obst_image.get_rect(topleft = (WIDTH, passage_height - passage_width/2 - 400))

def window():
    SCREEN.fill(light_blue)
    SCREEN.blit(player_image, (PLAYER.x, PLAYER.y))
    SCREEN.blit(down_obst_image, (down_obst.x, down_obst.y))
    SCREEN.blit(up_obst_image, (up_obst.x, up_obst.y))
    pygame.display.update()
    

def player_movement(player: pygame.Rect, pressed_key):
    gravity = 6
    position = pygame.math.Vector2(player.topleft)
    position.y += gravity
    player.y = round(position.y)

    if pressed_key[pygame.K_SPACE]:
        player.y += -20

    if player.colliderect(down_obst) or player.colliderect(up_obst):
        pygame.quit()


def obstacles_movement(down_obst, up_obst):
    speed = 3

    down_obst_pos = pygame.math.Vector2(down_obst.topleft)
    down_obst_pos.x -= speed
    down_obst.x = round(down_obst_pos.x)
 
    up_obst_pos = pygame.math.Vector2(up_obst.topleft)
    up_obst_pos.x -= speed
    up_obst.x = round(up_obst_pos.x)


def main():
    run = True 
    while run: #while run == True:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pressed_key = pygame.key.get_pressed()

        window()
        obstacles_movement(down_obst, up_obst)
        player_movement(PLAYER, pressed_key)
        
    pygame.quit()

if __name__ == "__main__":
    main()
