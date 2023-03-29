import numpy as np
import pygame 
import os
from player import Player
from dementor import Predator
from potion import Potion
import random
import time 

## Define the constants 
FPS = 120
WIDTH, HEIGHT = 1400, 1000
INIT_FUEL = 10
MAX_SPELLS = 10
SPELL_VEL = 5
 
# Initialize Pygame
pygame.init()

## Set up the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mayhem")

## Load images
harry = pygame.image.load(os.path.join("Assets", "harry.png"))
SPACE1 = pygame.image.load(os.path.join("Assets", "test1.jpg"))
voldemort = pygame.image.load(os.path.join("Assets", "vol.png"))
dementor = pygame.image.load(os.path.join("Assets", "dem.png"))
potion1 = pygame.image.load(os.path.join("Assets", "potion1.png"))
potion2 = pygame.image.load(os.path.join("Assets", "potion2.png"))

## Load soundclips 
main_sound = pygame.mixer.Sound(os.path.join('Assets', 'main_sound.mp3'))


## Resize images 
harry_WIDTH, harry_HEIGHT = int(harry.get_width() * 0.25), int(harry.get_height() * 0.25)
harry1 = pygame.transform.scale(harry, (harry_WIDTH, harry_HEIGHT))
voldemort1 = pygame.transform.scale(voldemort, (harry_WIDTH, harry_HEIGHT))
dementor1 = pygame.transform.scale(dementor, (harry_WIDTH, harry_HEIGHT))
potion11 = pygame.transform.scale(potion1, (harry_WIDTH*0.5, harry_HEIGHT*0.5))
potion22 = pygame.transform.scale(potion2, (harry_WIDTH*0.5, harry_HEIGHT*0.5))
SPACE = pygame.transform.scale(SPACE1, (WIDTH, HEIGHT))


## Function to run the main game-loop
def main():
    
    # Set speed of game-loop (FPS)
    clock = pygame.time.Clock()

    ## Create the player objects 
    player1 = Player(100, 500, harry_WIDTH, harry_HEIGHT, SPACE, harry1, HEIGHT, WIDTH, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2 = Player(950, 500, harry_WIDTH, harry_HEIGHT, SPACE, voldemort1, HEIGHT, WIDTH, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    player_group = pygame.sprite.Group()
    player_group.add(player1)
    player_group.add(player2)

    # Create the dementor
    predator = Predator(500, 500, dementor1, WIDTH, HEIGHT, [player1, player2], 25)

    # Create the potions
    potion_group = pygame.sprite.Group()
    potion_group.add(Potion(200,300, potion11))
    potion_group.add(Potion(500,500, potion22))
    potion1 = Potion(900,300, potion11)
    
    voldemort_spells = []
    harry_spells = []

    YELLOW_HIT = pygame.USEREVENT + 1 #Create two separate events, its just a number
    RED_HIT = pygame.USEREVENT + 2     

    def handle_spells(harry_spells, voldemort_spells, harry, voldemort):
        for spell in harry_spells:
            spell.x += SPELL_VEL
            if voldemort.rect.colliderect(spell): 
                pygame.event.post(pygame.event.Event(RED_HIT))
                harry_spells.remove(spell)
            
            #check if spells is off the screen
            elif spell.x > WIDTH:
                harry_spells.remove(spell)

        
        for spell in voldemort_spells:
            spell.x -= SPELL_VEL
            if harry.rect.colliderect(spell): 
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                voldemort_spells.remove(spell)
            elif spell.x < 0:
                voldemort_spells.remove(spell)



    # Initialize the time of the last potion spawn
    last_potion_spawn_time = 0    

    ## Game-loop
    run = True 
    while run:
        clock.tick(FPS)

        # Iterate over all game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Handle spells for each player
            if pygame.key.get_pressed()[pygame.K_SPACE] and len(harry_spells) < MAX_SPELLS:
                spell = pygame.Rect(player1.pos.x + harry_WIDTH*0.2, player1.pos.y + (harry_HEIGHT*0.5)//2, 50, 4)
                harry_spells.append(spell)

            if pygame.key.get_pressed()[pygame.K_m] and len(voldemort_spells) < MAX_SPELLS:
                spell = pygame.Rect(player2.pos.x - harry_WIDTH*0.2 , player2.pos.y - (harry_HEIGHT*0.5)//2, 50, 4)
                voldemort_spells.append(spell)

        # Main sound theme 
        main_sound.play()

        ## Draw background and constant structures
        WIN.blit(SPACE, (0,0))

        # Get all the keys currently being pressed
        keys_pressed = pygame.key.get_pressed()

        ## Update player position based on keys pressed
        player_group.update(keys_pressed, potion_group)

        ## Draw players
        ####################################FIX NEEDED#############################
        #player_group.draw(WIN)
        player1.draw(WIN)
        player2.draw(WIN)
        


        ## Handle spells 
        handle_spells(harry_spells, voldemort_spells, player1, player2)


        ## Initial health stats 
        harry_health = 3
        voldemort_health = 3

        ## Update movement and draw dementor
        predator.update(WIDTH, HEIGHT)
        predator.draw(WIN)


        ## Spawn potions at random intervals 
        current_time = pygame.time.get_ticks()
        if current_time - last_potion_spawn_time > random.uniform(5000,10000):
            last_potion_spawn_time = current_time
            if len(potion_group) == 0:
                potion_group.add(Potion(random.randint(30,1300), random.randint(30, 900), potion11))



        for potion in potion_group:
            potion.check_collision(player_group)

        potion_group.draw(WIN)
        
        ## Display health and spell count 
        font = pygame.font.SysFont("calibri",20)
        player1_health = font.render("Harry Potter Health: " +str(harry_health), True, (50, 255, 100))
        player1_spellcount = font.render("Harry Potter broomstick fuel: " +str(player1.fuel), True, (50, 255, 100))

        player2_health = font.render("Voldemort Health: " +str(voldemort_health), True, (255, 50, 50))
        player2_spellcount = font.render("Voldemort broomstick fuel: " +str(player2.fuel), True, (255, 50, 50))

        WIN.blit(player1_health,(10,40))
        WIN.blit(player1_spellcount,(10,70))
        WIN.blit(player2_health,(1100,40))
        WIN.blit(player2_spellcount,(1100,70))


        #Drawing the bullets
        for spell in harry_spells:
            pygame.draw.rect(WIN, (255,0,0), spell)
        
        for spell in voldemort_spells:
            pygame.draw.rect(WIN, (0,255,0), spell)
        

        # Update game display
        pygame.display.update()

        # Check if player1 is out of fuel
        if player1.fuel == 0:
            WIN.fill((0, 0, 0))
            l1 = font.render("Harry's broomstick died", True, (255, 0, 0))
            WIN.blit(l1, (WIDTH//2 - 150, HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(15000)
            run = False

        # Check if player1 is out of fuel
        if player2.fuel == 0:
            WIN.fill((0, 0, 0))
            l1 = font.render("Voldemort's broomstick died horribly shhhhhhhh pofffff", True, (255, 0, 0))
            WIN.blit(l1, (WIDTH//2 - 400, HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(15000)
            run = False


    ## Quit pygame and exit 
    pygame.quit()
    exit()



if __name__ == "__main__":
    main()


        


