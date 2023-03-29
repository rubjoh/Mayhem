from pygame.math import Vector2
import pygame
import random



## Pygame events for spells
SPELL_HIT = pygame.USEREVENT + 1 


class Player(pygame.sprite.Sprite):
    GRAVITY = 0.1
    MAX_SPEED = 2

    def __init__(self, x_pos, y_pos, width, height, background, image, screen_height, screen_width, up, down, left, right):
        super().__init__()
        self.image = image
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.vel = Vector2(0, 0)
        self.bg = background
        self.pos = Vector2(x_pos, y_pos)
        self.h = height
        self.w = width
        self.HEIGHT = screen_height
        self.WIDTH = screen_width
        self.up = up
        self.down = down
        self.left = left 
        self.right = right
        self.fuel = 100
        self.time_elapsed = 0
        self.spells = []
        self.spell_delay = 0
        self.spell_cooldown = 500




    def update(self, keys_pressed, potions):
        '''
        Method for handling the movement of the sprites.
        '''
        acceleration = Vector2(0, self.GRAVITY)
        if keys_pressed[self.left]:
            acceleration += Vector2(-1, 0)
        if keys_pressed[self.right]:
            acceleration += Vector2(1, 0)
        if keys_pressed[self.up]:
            acceleration += Vector2(0, -1)
        if keys_pressed[self.down]:
            acceleration += Vector2(0, 1)

        self.vel += acceleration
        self.vel.x = max(-self.MAX_SPEED, min(self.vel.x, self.MAX_SPEED)) # limit x speed
        self.vel.y = max(-self.MAX_SPEED, min(self.vel.y, self.MAX_SPEED)) # limit y speed

        new_pos = self.pos + self.vel

        if new_pos.x - 65 < 0:
            new_pos.x = 65
            self.vel.x = 0
        elif new_pos.x > self.WIDTH - 65:
            new_pos.x = self.WIDTH - 65
            self.vel.x = 0

        if new_pos.y - 80 < 0:
            new_pos.y = 80
            self.vel.y = 0
        elif new_pos.y > self.HEIGHT - 80:
            new_pos.y = self.HEIGHT - 80
            self.vel.y = 0

        self.pos = new_pos

        # Check for collisions with potions and update fuel attribute
        for potion in potions: 
            if (potion.pos - self.pos).length() < 75:
                self.fuel += 10

        # Update fuel 
        self.time_elapsed += 10
        if self.time_elapsed >= 1000:  # If 1 second has elapsed
            self.fuel -= 1  # Subtract 1 from fuel
            self.time_elapsed = 0  # Reset time_elapsed to 0


    def draw(self, surface):
        '''
        Method for drawing the sprites and handling rotion of the
        images.
        '''
        angle = self.vel.angle_to(Vector2(0, -1))
        rotated_image = pygame.transform.rotate(self.image, angle)
        rect = rotated_image.get_rect()
        rect.center = (int(self.pos.x), int(self.pos.y))
        surface.blit(rotated_image, rect)

    def handle_spells(self, player, button):
        '''
        Method for handling the spells/bullets
        '''
        # decrement the spell_delay timer
        if self.spell_delay > 0:
            self.spell_delay -= 1
        
        # handle firing spells/bullets
        if pygame.key.get_pressed()[button] and self.spell_delay <= 0:
            # create a new spell/bullet object and add it to the list
            spell = pygame.Rect(self.rect.x + self.WIDTH, self.rect.y + self.HEIGHT//2, 20, 8)
            self.spells.append(spell)
            self.spell_delay = self.spell_cooldown  # set the delay timer to the cooldown time
        
        # update the positions of all the spells/bullets
        for spell in self.spells:
            spell.x += int(self.vel.x * 2)
            spell.y += int(self.vel.y * 2)

            
            # check for collisions with enemies or other objects
            if spell.colliderect(player.rect):
                # handle the collision here
                pass
            
            # remove spells/bullets that are off the screen
            elif spell.x > self.WIDTH or spell.y > self.HEIGHT:
                self.spells.remove(spell)




