import pygame

pygame.init()

WIDTH = 480
HEIGHT = 800
FRAMERATE = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

def main():
    run = True 
    while run: #while run == True:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
