import pygame, sys
from drop import RainDrop

class RainGame():
    '''Simple rain game.'''

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rain")

        self.rain_drops = pygame.sprite.Group()
        self._create_rain_drops()

    def run_game(self):
        '''The main loop for the game.'''
        while True:
            self._check_events()
            self.screen.fill((20, 40, 80))
            self.rain_drops.draw(self.screen)
            self._update_rain_drops()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        '''Respond to quitting'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _create_rain_drops(self):
        '''Create the row of rain_drops.'''
        rain_drop = RainDrop(self)
        rain_drop_width, rain_drop_height = rain_drop.rect.size

        current_x, current_y = rain_drop_width, rain_drop_height

        while current_x < (self.screen.get_width() - rain_drop_width):
            self._create_rain_drop(current_x, current_y)
            current_x += 2 * rain_drop_width

        current_x = rain_drop_width

    def _create_rain_drop(self, x_position, y_position):
        '''Create an raindrop and place it in the row.'''
        new_rain_drop = RainDrop(self)
        new_rain_drop.x = x_position
        new_rain_drop.rect.x = x_position 
        new_rain_drop.rect.y = y_position 
        self.rain_drops.add(new_rain_drop)

    def _update_rain_drops(self):
        '''Move the rain drops down.'''
        self.rain_drops.update()


if __name__ == '__main__':
    s = RainGame()
    s.run_game()

