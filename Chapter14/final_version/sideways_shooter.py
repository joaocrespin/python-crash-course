import pygame, sys
from time import sleep

from ship import Ship
from bullet import Bullet
from star import Star
from settings import Settings
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats


class SidewaysShooter:
    '''The main class of Sideways Shooter.'''
    
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self, 'Play')

        self._create_difficulty_buttons()

    
    def _create_difficulty_buttons(self):
        '''Make difficulty level buttons.'''
        self.easy_button = Button(self, 'Easy')
        self.medium_button = Button(self, 'Medium')
        self.hard_button = Button(self, 'Hard')

        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5*self.play_button.rect.height)
        self.easy_button.update_position()

        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button.update_position()

        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.hard_button.update_position()

    def run_game(self):
        '''Main game loop.'''
        while True :
            self._handle_events()

            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_stars()

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
                    self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''Start a new game when the player clicks play.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        '''Initialize the game.'''
        self.settings.initialize_dynamic_settings()

        self.stats.reset_stats()
        self.sb.prep_images()
        self.game_active = True

        self.bullets.empty()
        self.stars.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)

    def _check_difficulty_buttons(self, mouse_pos):
        '''Change the difficulty level.'''
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(
                mouse_pos)
        diff_button_clicked = self.hard_button.rect.collidepoint(
                mouse_pos)
        if easy_button_clicked:
            self.settings.difficulty_level = 'easy'
        elif medium_button_clicked:
            self.settings.difficulty_level = 'medium'
        elif diff_button_clicked:
            self.settings.difficulty_level = 'hard'
                
    def _handle_keydown(self, event):
        '''Deals with keydown based events.'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
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

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        new_bullet = Bullet(self)
        self._play_bullet_sound_effect()
        self.bullets.add(new_bullet)

    def _play_bullet_sound_effect(self):
        '''Play the laser shooting sound effect.'''
        pygame.mixer.init()
        pygame.mixer.music.load('spaceship_shooting_laser.wav')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()

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
            for stars in collisions.values():
                self.stats.score += self.settings.star_points * len(stars)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.stars:
            self._new_level()
            
    def _new_level(self):
        '''Destroy existing bullets, create a new fleet and level up.'''
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        self.stats.level += 1
        self.sb.prep_level()

    def _update_stars(self):
        '''Update the positions of all stars in the fleet.'''
        self._check_fleet_edges()
        self.stars.update()

        if pygame.sprite.spritecollideany(self.ship, self.stars):
            self._ship_hit()

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
            star.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self): 
        '''Respond to the ship being hit by an star.'''
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.stars.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        '''Handle screen related updates.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()  
        self.stars.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    shooter = SidewaysShooter()
    shooter.run_game()