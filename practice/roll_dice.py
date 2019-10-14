from random import randint


class RollDice:
    '''class to manage roll dice'''
    def __init__(self,dice_sides=6):
        self.dice_sides=dice_sides
        self.roll_dice()

    def roll_dice(self):
        return randint(1,self.dice_sides)
