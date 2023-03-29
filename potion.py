import pygame
from pygame import Vector2

class Potion(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        #self.rect.topleft = (x,y)
        self.pos = Vector2(x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def check_collision(self, players):
        for player in players: 
            if (self.pos - player.pos).length() < 75:
                print("COLLISION DETECTED")
                self.kill()
    
    def update(self, player):
        if self.rect.colliderect(player.rect):
            print("DEAD MAN WALKING")
            self.kill()



