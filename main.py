import pygame
from src import settings

pygame.init()

# skapa skärmen där höjden är 900 och breden är 700
skärm = pygame.display.set_mode(settings.SCREEN_SIZE)



# titeln på spelet
pygame.display.set_caption("Pygame krig game shit duc denis shir eli shit joeli shit")

run = True
while run:
    for pygame_event in pygame.event.get():
        if pygame_event.type == pygame.QUIT:
            run = False


    #färgen på skärmen  "röd", " grön", "blå"       
    skärm.fill((0, 0, 0))

    #uppdatera skärmen
    pygame.display.flip()

pygame.quit()