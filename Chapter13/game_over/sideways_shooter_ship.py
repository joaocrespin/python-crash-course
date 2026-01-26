import pygame 

class Ship:
    '''A class to manage a Ship.'''

    def __init__(self, sh_game):
        self.screen = sh_game.screen
        self.settings = sh_game.settings
        self.screen_rect = sh_game.screen.get_rect()

        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Update the Ship position based on the moviment flag.'''
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed


    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the ship on the screen.'''
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)