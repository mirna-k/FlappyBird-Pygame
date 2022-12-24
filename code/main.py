import pygame

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

# ELEMENTS
PLAYER = pygame.Rect(WIDTH/4-25, HEIGHT/2, 50, 50)

def window():
    SCREEN.fill(light_blue)
    pygame.draw.rect(SCREEN, black, PLAYER)
    pygame.display.update()

def player_movement(player, pressed_key):
    gravity = 6
    position = pygame.math.Vector2(player.topleft)
    position.y += gravity
    player.y = round(position.y)

    if pressed_key[pygame.K_SPACE]:
        player.y += -35


def main():
    run = True 
    while run: #while run == True:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pressed_key = pygame.key.get_pressed()

        window()
        player_movement(PLAYER, pressed_key)
        
    pygame.quit()

if __name__ == "__main__":
    main()
