import numpy as np
import pygame 
import os



## Define the constants 
FPS = 120
WIDTH, HEIGHT = 1400, 1000
INIT_FUEL = 10
 
# Initialize Pygame
pygame.init()

## Set up the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mayhem")

## Load images
harry = pygame.image.load(os.path.join("Assets", "harry.png"))
SPACE1 = pygame.image.load(os.path.join("Assets", "test1.jpg"))
voldemort = pygame.image.load(os.path.join("Assets", "voldemort.png"))







## Resize images 
harry_WIDTH, harry_HEIGHT = int(harry.get_width() * 0.25), int(harry.get_height() * 0.25)
harry1 = pygame.transform.scale(harry, (harry_WIDTH, harry_HEIGHT))
voldemort1 = pygame.transform.scale(voldemort, (harry_WIDTH, harry_HEIGHT))
SPACE = pygame.transform.scale(SPACE1, (WIDTH, HEIGHT))




## Function to run the main game-loop
def main():
    
    # Set speed of game-loop (FPS)
    clock = pygame.time.Clock()

    ## Game-loop
    run = True
    while run:
        clock.tick(FPS)

        ## Draw background and constant structures
        WIN.blit(SPACE, (0,0))
        WIN.blit(harry1, (100, 500))
        WIN.blit(voldemort1, (900, 500))

        # Iterate over all game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update game display
        pygame.display.update()


    ## Quit pygame and exit 
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()


        


