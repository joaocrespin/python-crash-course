import pygame, sys
from time import sleep
from sideways_shooter_stats import Stats
from sideways_shooter_ship import Ship
from sideways_shooter_bullet import Bullet
from sideways_shooter_star import Star
from sideways_shooter_settings import Settings

# TODO: Display the score

class SidewaysShooter:
    '''The main class of Sideways Shooter'''
    
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.stats = Stats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()

        self.score = 0

        self.game_active = True

    def run_game(self):
        '''Main game loop.'''
        while True:
            self._handle_events()
            
            if self.game_active:
                self._update_bullet()
                self._update_stars()
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
            if bullet.rect.right > self.screen.get_width():
                self.bullets.remove(bullet)
            
        self._check_bullet_star_collisions()

    def _check_bullet_star_collisions(self):
        '''Respond to bullet-star collisions.'''
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.stars, True, True)
        
        if collisions:
            self.score += 1
            #print(self.score)
        
        if not self.stars:
            # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_stars(self):
        '''Update the positions of all stars in the fleet.'''
        self._check_fleet_edges()
        self.stars.update()

        if pygame.sprite.spritecollideany(self.ship, self.stars):
            self._ship_hit()
        
        self._check_stars_left()

    def _create_fleet(self):
        '''Create the fleet of stars'''
        star = Star(self)
        star_width, star_height = star.rect.size

        start_x = self.settings.screen_width - 2 * star_width
        current_x, current_y = start_x, star_height

        while current_x > 2 * star_width:
            while current_y < (self.settings.screen_height - 2 * star_height):
                self._create_star(current_x, current_y)
                current_y += 2 *star_height

            current_y = star_height
            current_x -= 2 * star_width

    def _create_star(self, x_position, y_position):
        '''Create an star and place it in the row'''
        new_star = Star(self)
        new_star.y = y_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _check_fleet_edges(self):
        '''Change the direction if star is on edge.'''
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop the entire fleet and change fleet direction.'''
        for star in self.stars.sprites():
            star.rect.x -= self.settings.fleet_move_speed
        self.settings.fleet_direction *= -1

    def _check_stars_left(self):
        '''Check if an star has reached the bottom of the screen.'''
        for star in self.stars.sprites():
            if star.rect.left <= 0:
                # Same behavior as HIT
                self._ship_hit()
                break

    def _ship_hit(self):
        '''Respond to the ship being hit by an star.'''

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.stars.empty()

            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            print(f'Final score: {self.score}')

    def _update_screen(self):
        '''Handle screen related updates.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()  
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    shooter = SidewaysShooter()
    shooter.run_game()