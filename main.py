import pygame
from src import settings

def main():
    pygame.init()

    # Game title
    pygame.display.set_caption("Python Game Project")

    environment = pygame.display.set_mode(settings.SCREEN_SIZE)
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        # Update environment
        environment.fill(settings.BACKGROUND_COLOR) # maybe this shouldnt be here but outside the while loop
        pygame.display.flip()

if __name__ == "__main__":
    main()