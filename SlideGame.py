import numpy as np

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 5: Eight Puzzle
# Caden Steele
# DUE DECEMBER 4TH.....
# ---------------------------------------
# A tile sliding game.
# ---------------------------------------

class EightPuzzle:

    def __init__(self):
        self.solution = np.array([1,2,3,4,5,6,7,8," "])
        self.solution = self.solution.reshape(3,3)
        print(self.solution)

    def __str__(self):
        separator = "+-+-+-+\n"
        answer = separator
        for row in range(3):
            for col in range(3):
                answer += "|" + str(self.puzzle[row][col])
            answer += "|\n"
            answer += separator
        return answer

    def puzzle_1(self):
        self.puzzle = np.array([1,2,3,4,5,6,7,8," "])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 2
        self.blank_y = 2
        

    def puzzle_2(self):
        self.puzzle = np.array([4,1,3,7,2,5,8," ", 6])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 2
        self.blank_y = 1

    def puzzle_3(self):
        self.puzzle = np.array([5,4," ",7,1,8,3,6,2])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 0
        self.blank_y = 2

        
    def swap(self, x1, y1, x2, y2):
        self.puzzle[x1][y1], self.puzzle[x2][y2] = \
                             self.puzzle[x2][y2], self.puzzle[x1][y1]

# ---------------------------------------
# Do not change anything above this line
# ---------------------------------------


    def is_puzzle_solved(self):
        if (self.solution == self.puzzle).all():
            return True


    def move_blank(self):
        direction = input("Enter a direction to move the blank: ")
        loc = [0,0]
        newLoc = [0,0]
        r = -1

    #find coordinate of blank space
        for i in self.puzzle:
            r += 1
            c = -1
            for j in i:
                c += 1
                if j == ' ':
                    loc = [c, r]
                    newLoc[0] = c
                    newLoc[1] = r
                    
    #Change location of blank space               
        if direction.lower() == "left":
            if int(newLoc[0]) - 1 >= 0:
                newLoc[0] = int(newLoc[0]) - 1
                self.puzzle[loc[1]][loc[0]] = self.puzzle[newLoc[1]][newLoc[0]]
                self.puzzle[newLoc[1]][newLoc[0]] = ' '
                
            else:
                print("That is not a valid move. Try again. \n")

        if direction.lower() == "right":
            if int(newLoc[0]) + 1 < 3:
                newLoc[0] = int(newLoc[0]) + 1
                self.puzzle[loc[1]][loc[0]] = self.puzzle[newLoc[1]][newLoc[0]]
                self.puzzle[newLoc[1]][newLoc[0]] = ' '
                
            else:
                print("That is not a valid move. Try again. \n")

        if direction.lower() == "up":
            if int(newLoc[1]) - 1 >= 0:
                newLoc[1] = int(newLoc[1]) - 1                
                self.puzzle[loc[1]][loc[0]] = self.puzzle[newLoc[1]][newLoc[0]]
                self.puzzle[newLoc[1]][newLoc[0]] = ' '
                
            else:
                print("That is not a valid move. Try again. \n")

        if direction.lower() == "down":
            if int(newLoc[1]) + 1 < 3:
                newLoc[1] = int(newLoc[1]) + 1                
                self.puzzle[loc[1]][loc[0]] = self.puzzle[newLoc[1]][newLoc[0]]
                self.puzzle[newLoc[1]][newLoc[0]] = ' '
                
            else:
                print("That is not a valid move. Try again. \n")

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def solve(puzzle):
    steps = 0
    print("Puzzle:\n")
    print(puzzle)
    while not puzzle.is_puzzle_solved():
        puzzle.move_blank()
        print(puzzle)
        steps += 1
    print("Congratulations - you solved the puzzle in", steps, "steps!\n")
        

def main():
    puzzle = EightPuzzle()
    puzzle.puzzle_1()
    solve(puzzle)
    puzzle.puzzle_2()
    solve(puzzle)
    puzzle.puzzle_3()
    solve(puzzle)
    
# ---------------------------------------

main()
