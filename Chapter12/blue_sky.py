import pygame, sys

class BlueSky:
    '''Represent a blue sky.'''
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            self.screen.fill((15,70,115))
            pygame.display.flip()


if __name__ == '__main__':
    bluesky = BlueSky()
    bluesky.run_game()