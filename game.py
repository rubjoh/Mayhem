import numpy as np
import pygame 
import os



## Define the constants 
FPS = 120
WIDTH, HEIGHT = 1200, 900

# Initialize Pygame
pygame.init()

## Set up the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mayhem")

## Load images
boid = pygame.image.load(os.path.join("Assets", "test.png"))
SPACE1 = pygame.image.load(os.path.join("Assets", "the11.jpg"))
predator = pygame.image.load(os.path.join("Assets", "ufo.png"))
obstacle = pygame.image.load(os.path.join("Assets", "planet2.png"))
obstacle_2 = pygame.image.load(os.path.join("Assets", "planet1.png"))
obstacle_3 = pygame.image.load(os.path.join("Assets", "planet3.png"))
obstacle_4 = pygame.image.load(os.path.join("Assets", "planet4.png"))
obstacle_5 = pygame.image.load(os.path.join("Assets", "planet5.png"))
obstacle_6 = pygame.image.load(os.path.join("Assets", "planet6.png"))

## Resize images 
boid_WIDTH, boid_HEIGHT = int(boid.get_width() * 0.08), int(boid.get_height() * 0.08)
boid1 = pygame.transform.scale(boid, (boid_WIDTH, boid_HEIGHT))
predator1 = pygame.transform.scale(predator, (100, 100))
SPACE = pygame.transform.scale(SPACE1, (WIDTH, HEIGHT))
obstacle1 = pygame.transform.scale(obstacle, (100, 100))
obstacle2 = pygame.transform.scale(obstacle_2, (100, 100))
obstacle3 = pygame.transform.scale(obstacle_3, (150, 150))
obstacle4 = pygame.transform.scale(obstacle_4, (120, 120))
obstacle5 = pygame.transform.scale(obstacle_5, (150, 150))
obstacle6 = pygame.transform.scale(obstacle_6, (120, 150))


## Function to run the main game-loop
def main():
    
    # Set speed of game-loop (FPS)
    clock = pygame.time.Clock()

    ## Game-loop
    run = True
    while run:
        clock.tick(FPS)

        ## Draw background and constant structures



    
        # Update game display
    
    ## Quit pygame and exit 
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()


        


