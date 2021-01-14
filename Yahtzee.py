import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 10
# November 12, 2018
# Caden Steele
# -------------------------------------------------
# Not all of this file was written by myself
#--------------------------------------------------

###############
## Class to hold the value of a single die
###############

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

###############
## Class to hold the value of a single die
###############
class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def rollDice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()

    def countDiceValues(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        self.counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            self.counts[roll] += 1

    def determineYahtzee(self):
        for i in self.rolls:
            if self.rolls[0] == self.rolls[1] and self.rolls[1] == self.rolls[2]:
                if self.rolls[2] == self.rolls[3]and self.rolls[3] == self.rolls[4]:
                    print("YAHTZEE " + str(self.rolls))
                    return True
    
    def determineStraight(self):

        self.rolls.sort()
        if self.rolls[0] < self.rolls[1] and self.rolls[1] < self.rolls[2]:
            if self.rolls[2] < self.rolls[3] and self.rolls[3] < self.rolls[4]:
                print("Straight " + str(self.rolls))
                return True
                   
    def determineFullHouse(self):    
        check3 = False
        check2 = False
        
        for i in self.counts:
                if i == 3:
                    check3 = True
                elif i == 2:
                    check2 = True
                if check3 == True and check2 == True:
                    print("FullHouse " + str(self.rolls))
                    return True

        
    def getCards(self):
        return self.rolls
    

def main():
    y = Yahtzee()
    nothing = yahtzeeCount = fullCount= straightCount = 0
    for i in range(200):
        y.rollDice()
        y.countDiceValues()
        ##################
        
        yahtzeeCheck = y.determineYahtzee()
        fullCheck = y.determineFullHouse()
        straightCheck = y.determineStraight()
        
        if fullCheck == True:
            fullCount += 1
        if yahtzeeCheck == True:
            yahtzeeCount += 1
        if straightCheck == True:
            straightCount += 1
            

    nothing = 200 - (fullCount + yahtzeeCount + straightCount)
    print("Yahtzee", str(yahtzeeCount), "Fullhouse", str(fullCount), "Straights", str(straightCount), "Losers", str(nothing))     
main()
