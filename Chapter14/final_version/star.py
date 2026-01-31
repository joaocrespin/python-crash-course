import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    '''A class to represent a single star.'''
    def __init__(self, sh_game):
        super().__init__()

        self.screen = sh_game.screen
        self.settings = sh_game.settings

        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edges(self):
        '''Return true if star is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)
    
    def update(self):
        '''Move the star to the right.'''
        self.y += self.settings.star_speed * self.settings.fleet_direction
        self.rect.y = self.y
