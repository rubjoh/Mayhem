from pygame.math import Vector2
import pygame
import random


class Predator(pygame.sprite.Sprite):

    def __init__(self, x, y, image, screen_width, screen_height, players, borders):
        self.position = Vector2(x,y)
        self.velocity = Vector2(random.randint(-2,2),random.randint(-2,2))
        self.image = image
        self.w = screen_width
        self.h = screen_height
        self.players = players
        self.borders = borders
        self.neighborhood = 500

    def draw(self, surface):

        # Calculate the angle of rotation based on the direction of the velocity vector
        angle = self.velocity.angle_to(Vector2(0, -1))

        # Rotate the image of the player
        rotated_image = pygame.transform.rotate(self.image, angle)

        # Get the rectangle that encloses the rotated image
        rect = rotated_image.get_rect()

        # Set the center of the rectangle to the position of the player
        rect.center = (int(self.position.x), int(self.position.y))

        # Draw the rotated image on the surface
        surface.blit(rotated_image, rect)

    def cohesion(self):
        '''
        Method that moves the dementor to the mean of the players in it's neighborhood
        '''
        ## Calculate mean position of the players
        count = 0
        mean_pos = Vector2(0, 0)
        for player in self.players:
            # Check if the player is in the predators neighborhood
            if (player.pos - self.position).length() < self.neighborhood:
                mean_pos += player.pos
                count += 1
        if count > 0:
            mean_pos /= count

        # Calculate the vector towards the mean position and nomalize it 
        towards_mean = (mean_pos - self.position).normalize()

        # Adjust the velocity vector towards the mean position
        # Weight controls the strength of the cohesion behavior
        weight = 0.06
        self.velocity += towards_mean * weight
    


    def update(self, width, height):
        '''Method that controls the movement of the predators'''

        # Update the position based on velocity
        self.position += self.velocity

        ## Check if predator is out of the screen and flip the position to opposite side
        # Check left border
        if self.position.x < 0:
            self.position.x = width
        # Check right border
        elif self.position.x > width:
            self.position.x = 0
            
        # Check top and bottom borders
        self.position.y = max(self.position.y, self.borders + 40)
        self.position.y = min(self.position.y, height - self.borders - 40)
        if self.position.y == self.borders + 40 or self.position.y == height - self.borders - 40:
            self.velocity.y = -self.velocity.y

        # Calling method for cohesion behavior towards players
        self.cohesion()

        # Limit the speed of the dementor
        max_speed = 1.1
        if self.velocity.length() > max_speed:
            self.velocity.scale_to_length(max_speed)

        # Limit the acceleration of the dementor
        max_acceleration = 0.4
        if self.velocity.length() > 0:
            acceleration = self.velocity.normalize() * max_acceleration
            self.velocity += acceleration
            if self.velocity.length() > max_speed:
                self.velocity.scale_to_length(max_speed)
    

