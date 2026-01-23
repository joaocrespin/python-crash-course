import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship.'''

    def __init__(self, sh_game):
        super().__init__()
        self.screen = sh_game.screen
        self.color = (255,255,0)

        self.rect = pygame.Rect((0, 0, 15, 3))
        self.rect.midright = sh_game.ship.rect.midright


        self.x = float(self.rect.x)

    def update(self):
        '''Move the bullet on the screen.'''
        self.x += 2
        self.rect.x = self.x
    
    def draw_bullet(self):
        '''Draw the bullet to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)
