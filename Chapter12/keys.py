import pygame, sys

class Key:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Key")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
            

            self.screen.fill((90, 30, 90))
            pygame.display.flip()
    

if __name__ == '__main__':
    key = Key()
    key.run_game()