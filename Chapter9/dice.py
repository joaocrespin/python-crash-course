from random import randint

class Die:
    '''A simple class that models a dice'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        '''Roll the dice and return a number between 1 and the amount of sides'''
        return randint(1, self.sides)
    
dice_one = Die()
print("\n10 D6 rolls:")
for _ in range(10):
    print(dice_one.roll_die())

dice_two = Die(10)
print("\n10 D10 rolls:")
for _ in range(10):
    print(dice_two.roll_die())

dice_three = Die(20)
print("\n10 D20 rolls:")
for _ in range(20):
    print(dice_three.roll_die())