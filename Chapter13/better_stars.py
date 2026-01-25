import pygame, sys
from star import Star
from random import randint

class Stars:
    '''The main class of Stars.'''
    
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.screen.fill((35, 41, 115))
            self.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _create_stars(self):
        '''Create the fleet of stars.'''
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height

        while current_y < (self.screen.get_height() - 2 * star_height):
            while current_x < (self.screen.get_width() - star_width):
                self._create_star(current_x, current_y)
                current_x += star_width

            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        '''Create an star and place it in the row.'''
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position + randint(-10, 10)
        new_star.rect.y = y_position + randint(-10, 10)
        self.stars.add(new_star)




if __name__ == '__main__':
    s = Stars()
    s.run_game()