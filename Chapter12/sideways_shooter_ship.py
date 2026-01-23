import pygame 

class Ship:
    '''A class to manage a Ship.'''

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Update the Ship position based on the moviment flag.'''
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)