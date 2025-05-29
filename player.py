# Author: Jasmeen Kaur

import random
import math

class Player:
    def __init__(self, name, sign):
        self.name = name # player's name
        self.sign = sign # player's sign O or X
    def get_sign(self):
        sign = self.sign
        return sign
         # return an instance sign
    def get_name(self):
        name = self.name
        return name
        # return an instance name
    def choose(self, board):
 # prompt the user to choose a cell
 # if the user enters a valid string and the cell on the board is empty, update the board
 # otherwise print a message that the input is wrong and rewrite the prompt
 # use the methods board.isempty(cell), and board.set(cell, sign)
        valid_choices = ['A1', 'B1', "C1", 'A2', 'B2', "C2", 'A3', 'B3', "C3"]
        while True:
            cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper() 
            if cell in valid_choices:
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    break
                else:
                    print("You did not choose correctly.")
            else:
                print("You did not choose correctly.")


class AI(Player):
    def __init__(self, name, sign, board):
        self.board = board
        super().__init__(name, sign)
        if self.sign == "X":
            self.opposign = "0"
        else:
            self.opposign = "X"
 
    def choose(self, board):
        valid_choices = ['A1', 'B1', "C1", 'A2', 'B2', "C2", 'A3', 'B3', "C3"]
        while True:
            print(f'{self.name}, {self.sign}: Thinking...')
            cell = random.choice(valid_choices)
            if cell in valid_choices:
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    break
                else:
                    print("You did not choose correctly.")
            else:
                print("You did not choose correctly.")


class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
        self.possible_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
    
    def choose(self, board): 
        move = self.minimax(board, True, True)
        board.set(move, self.sign)
    
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            
            # self is a looser (opponent is a winner)
            else:
                return -1

        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
        min_score = math.inf
        max_score = -math.inf
        move = ""

        for cell in ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']:
            if self.board.isempty(cell):
                if self_player:
                    board.set(cell, self.sign)
                    score = MiniMax.minimax(self, board, False, False)
                    if score > max_score:
                        move = cell
                        max_score = score
                    board.set(cell, " ")

                else:
                    board.set(cell, self.opposign)
                    score = MiniMax.minimax(self, board, True, False)
                    if min_score > score:
                        move = cell
                        min_score = score
                    board.set(cell, " ")

        if start:
            return move
        elif self_player:
            return max_score
        else:
            return min_score
        
class SmartAI(AI):
    def __init__(self, name, sign):
        super().__init__(name, sign)
        self.opponent_sign = 'O' if self.sign == 'X' else 'X'

    def choose(self, board):
        print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        possible_choices = board.get_empty_cells()
        best_move = self._find_best_move(board, possible_choices, True)
        board.set(best_move, self.sign)
        print(best_move)

    def _find_best_move(self, board, possible_moves, maximizing_player):
        if board.is_game_over():
            return board.get_score(self.sign)

        best_move = None
        if maximizing_player:
            max_score = float('-inf')
            for move in possible_moves:
                board.set(move, self.sign)
                score = self._find_best_move(board, board.get_empty_cells(), False)
                board.reset_cell(move)
                if score > max_score:
                    max_score = score
                    best_move = move
        else:
            min_score = float('inf')
            for move in possible_moves:
                board.set(move, self.opponent_sign)
                score = self._find_best_move(board, board.get_empty_cells(), True)
                board.reset_cell(move)
                if score < min_score:
                    min_score = score
                    best_move = move

        return best_move
