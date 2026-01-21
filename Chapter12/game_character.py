import pygame, sys
from game_character_character import Character

class GameBackground:
    '''A simple background for a character to exist in.'''
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Character")

        self.character = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            self.screen.fill((90, 130, 75))
            self.character.blitme()
            pygame.display.flip()
            

if __name__ == '__main__':
    GameBackground = GameBackground()
    GameBackground.run_game()