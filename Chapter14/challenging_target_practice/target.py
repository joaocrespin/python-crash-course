import pygame
 
class Target:
    '''A class to manage a target.'''

    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = tp_game.settings
        self.color = self.settings.target_color

        self.rect = pygame.Rect(0, 0, self.settings.target_width,
            self.settings.target_height)
        self.center_target()

  
        self.direction = 1

    def move_target(self):
        '''Move the target steadily up and down.'''

        self.y += self.direction * self.settings.target_speed

        if self.rect.bottom > self.screen_rect.bottom:  
            self.rect.bottom = self.screen_rect.bottom
            self.direction = -1
        elif self.rect.top < 0:
            self.rect.top = 0
            self.direction = 1

        self.rect.y = self.y


    def center_target(self):
        '''Center the target on the right side of the screen.'''
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def draw_target(self):
        '''Draw the target to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)