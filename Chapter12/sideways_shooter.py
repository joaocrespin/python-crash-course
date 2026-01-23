import pygame, sys
from sideways_shooter_ship import Ship
from sideways_shooter_bullet import Bullet

class SidewaysShooter:
    '''The main class of Sideways Shooter'''
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Sideways Shooter")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''Main game loop.'''
        while True:
            self._handle_events()
            self.screen.fill((11, 17, 38))
            self._update_bullet()
            self._draw_bullet()
            self.ship.blitme()
            self.ship.update()
            pygame.display.flip()
    
    def _handle_events(self):
        '''Deals with keyboard and click based events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)
                
    def _handle_keydown(self, event):
        '''Deals with keydown based events.'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _handle_keyup(self, event):
        '''Deals with key up based events.'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullet(self):
        '''Update position of bullets and delete old ones.'''
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.right > 800:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _draw_bullet(self):
        '''Draw the bullets in the screen.'''
        for bullet in self.bullets.sprites():
                bullet.draw_bullet()

if __name__ == '__main__':
    shooter = SidewaysShooter()
    shooter.run_game()