import pygame
import random

pygame.init()

WIDTH = 480
HEIGHT = 800
FRAMERATE = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

# COLORS
light_blue = (173, 216, 230)
black = (5, 5, 5)
red = (227, 66, 52)

passage_width = random.randint(200, 350)
passage_height = random.randint(200, 600)

# ELEMENTS
PLAYER = pygame.Rect(WIDTH/4-25, HEIGHT/2, 50, 50)
down_obst = pygame.Rect((WIDTH, passage_height), (50, 600))
up_obst = pygame.Rect((WIDTH, passage_height - passage_width - 600), (50, 600))

def window():
    SCREEN.fill(light_blue)
    pygame.draw.rect(SCREEN, black, PLAYER)
    pygame.draw.rect(SCREEN, red, down_obst)
    pygame.draw.rect(SCREEN, red, up_obst)
    pygame.display.update()
    

def player_movement(player: pygame.Rect, pressed_key):
    gravity = 6
    position = pygame.math.Vector2(player.topleft)
    position.y += gravity
    player.y = round(position.y)

    if pressed_key[pygame.K_SPACE]:
        player.y += -25

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
