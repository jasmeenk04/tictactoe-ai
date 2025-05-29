# author: Jasmeen Kaur

class Board:
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        self.winner = ""

    def get_size(self):
        return self.size
    
    def get_winner(self):

        return self.winner

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        valid_choices = {'A1': 0, 'B1': 3, 'C1': 6, 'A2':1, 'B2':4, 'C2':7, 'A3':2,
        'B3':5, 'C3':8}
        index = valid_choices[cell]
        self.board[index] = sign
    def isempty(self, cell):
        valid_choices = {'A1': 0, 'B1': 3, 'C1': 6, 'A2':1, 'B2':4, 'C2':7, 'A3':2,
        'B3':5, 'C3':8}
        index = valid_choices[cell]
        return self.board[index] == " "
        # return True if the cell i empty (not marked with X or O)
    def isdone(self):
        done = False
        self.winner = " "
# check all game terminating conditions, if one of them is present, assign the var done to True
# depending on conditions assign the instance var winner to O or X
        if self.board[0] != " " and self.board[0] == self.board[1] == self.board[2]:
            done = True
            self.winner = self.board[0]
        elif self.board[3] != " " and self.board[3] == self.board[4] == self.board[5]:
            done = True
            self.winner = self.board[3]
        elif self.board[6] != " " and self.board[6] == self.board[7] == self.board[8]:
            done = True
            self.winner = self.board[6]
        elif self.board[2] != " " and self.board[2] == self.board[4] == self.board[6]:
            done = True
            self.winner = self.board[2]
        elif self.board[0] != " " and self.board[0] == self.board[4] ==self.board[8]:
            done = True
            self.winner = self.board[0]
        elif self.board[0] != " " and self.board[0] == self.board[3] == self.board[6]:
            done = True
            self.winner = self.board[3]
        elif self.board[1] != " " and self.board[1] == self.board[4] == self.board[7]:
            done = True
            self.winner = self.board[4]
        elif self.board[2] != " " and self.board[2] == self.board[5] == self.board[8]:
            done = True
            self.winner = self.board[5]
        if all(cell != " " for cell in self.board):
            done = True
            return done
    def show(self):
    # draw the board

        print()

        print(' A B C')

        print(' +---+---+---+')

        print('1| {} | {} | {} |'.format(self.board[0], self.board[3],self.board[6]))

        print(' +---+---+---+')

        print("2| {} | {} | {} |".format(self.board[1], self.board[4], self.board[7]))

        print(" +---+---+---+")

        print("3| {} | {} | {} |".format(self.board[2], self.board[5], self.board[8]))

        print(" +---+---+---+")
