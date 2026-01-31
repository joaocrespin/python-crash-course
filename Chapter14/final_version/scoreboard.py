import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    '''Report scoring information.'''

    def __init__(self, sh_game):
        self.sh_game = sh_game
        self.screen = sh_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sh_game.settings
        self.stats = sh_game.stats

        self.text_color = (240, 240, 240)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self):
        '''Prep everything at once.'''
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        '''Turn the score into an rendered image.'''
        # Round the score to the nearest multiple of 10
        rounded_score = round(self.stats.score, -1)

        # Insert commas at appropriate places
        score_str =  f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Draw the score to the screen.'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        '''Turn the high score into an rendered image.'''
    
        high_score = round(self.stats.high_score, -1)
        high_score_str =  f'{high_score:,}'

        self.high_score_image = self.font.render(high_score_str, True, 
            self.text_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        '''Check if there is a new high score.'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.stats.save_high_score(str(self.stats.score))
            self.prep_high_score()

    def prep_level(self):
        '''Turn the level into a rendered image.'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
            self.text_color, self.settings.bg_color)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''Show how many ships are left.'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.sh_game)
            ship.rect.right =  self.settings.screen_width - ship.rect.width * ship_number
            ship.rect.bottom =  self.settings.screen_height - 10
            self.ships.add(ship)