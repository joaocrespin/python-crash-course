import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
    '''A class to represent a rain drop.'''
    def __init__(self, rain_game):
        super().__init__()

        self.screen = rain_game.screen

        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edges(self):
        '''Return true if drop is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        return (self.rect.top >= screen_rect.bottom)
    
    def update(self):
        '''Move the drop down.'''
        self.y += 5
        self.rect.y = self.y
