from random import randint

class Die():
    '''Represent a single die.'''

    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        '''Return a random value between 1 and the number of sides.'''
        return randint(1, self.num_sides)