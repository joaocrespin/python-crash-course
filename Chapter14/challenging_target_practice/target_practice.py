import pygame, sys

from stats import Stats
from ship import Ship
from bullet import Bullet
from settings import Settings
from target import Target
from button import Button


class TargetPractice:
    '''The main class of Target Practice.'''
    
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Target Practice')

        self.stats = Stats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.target = Target(self)

        self.play_button = Button(self, 'Play')
        
        self.game_active = False

    def run_game(self):
        '''Main game loop.'''
        while True:
            self._handle_events()
            
            if self.game_active:
                self._update_bullet()
                self.target.move_target()
                self.ship.update()

            self._update_screen()
            self.clock.tick(60)
    
    def _handle_events(self):
        '''Deals with keyboard and click based events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
         
    def _handle_keydown(self, event):
        '''Deals with keydown based events.'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and self.game_active == False:
            self._start_game()

    def _handle_keyup(self, event):
        '''Deals with key up based events.'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        '''Check if the play button is available and  start the game.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        '''Start a new game.'''

        self.settings.initialize_dynamic_settings()

        self.stats.reset_stats()
        self.game_active = True

        self.bullets.empty()
        self.ship.center_ship()
        self.target.center_target()
        self.target.direction = 1

        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullet(self):
        '''Update position of bullets and delete old ones.'''
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen.get_width():
                self.bullets.remove(bullet)
                self._count_misses()

        self._check_bullet_target_collisions()

    def _count_misses(self):
        '''Check if the game shold end.'''
        self.stats.num_misses += 1
        if self.stats.num_misses >= self.settings.miss_limit:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_bullet_target_collisions(self):
        '''Check if the target was hit.'''
        collisions = pygame.sprite.spritecollide(self.target, self.bullets,
            True)
        if collisions:
            self.settings.increase_speed()


    def _update_screen(self):
        '''Handle screen related updates.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()  
        
        self.target.draw_target()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    shooter = TargetPractice()
    shooter.run_game()