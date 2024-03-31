import pygame
import math
pygame.init()
#### Hier stehen Funktionen und Klassen

def main():
    run = True
    player1 = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYER_HEIGHT, PLAYER_WIDTH)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        player_movement(player1, keys)
        draw(player1)
    pygame.quit()

def player_movement(player1, keys):
    if keys[pygame.K_a] and  player1.x - PLAYER_VELOCITY >= 0:
        player1.x -= PLAYER_VELOCITY
    if keys[pygame.K_d] and  player1.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
        player1.x += PLAYER_VELOCITY
    if keys[pygame.K_w] and player1.y - PLAYER_VELOCITY >= 0:
        player1.y -= PLAYER_VELOCITY
    if keys[pygame.K_s]and player1.y + PLAYER_VELOCITY + PLAYER_HEIGHT <= HEIGHT:
        player1.y += PLAYER_VELOCITY


def draw(player1):
    #WIN.blit(surf, (0, 0))
    WIN.fill((0,0,0))
    pygame.draw.rect(WIN,"red", player1)
    pygame.display.update()

###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    WIDTH, HEIGHT = 1000, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon :)")
    PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20
    PLAYER_VELOCITY = 5
    main()
