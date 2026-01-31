import pathlib

class GameStats:
    '''Track statistics for the game.'''

    def __init__(self, sh_game):
        self.settings = sh_game.settings
        self.reset_stats()

        # Never reset
        self.score_file = pathlib.Path('high_score.txt')
        try:
            stored_score = self.score_file.read_text()
        except FileNotFoundError:
            print('File not found!')
        else:
            self.high_score = int(stored_score)      


    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.ships_left = self.settings.ship_limit
        self.score =  0
        self.level = 1

    def save_high_score(self, new_high_score):
        '''Substitute the current high score with the new one.'''
        self.score_file.write_text(new_high_score)
        