class Stats:
    '''Track statistics for the game.'''

    def __init__(self, sh_game):
        self.settings = sh_game.settings
        self.reset_stats()


    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.ships_left = self.settings.ship_limit