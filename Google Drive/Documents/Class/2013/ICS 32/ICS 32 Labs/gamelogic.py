#Nicholas Fernando 12659548
import collections



        
class Board:

    def __init__(self, row: int, col: int):
        self._board = []
        self._copy = []
        self._row = row
        self._column = col
        self._none = ''
        self._black = 'B'
        self._white = 'W'

    def newboard(self):
        for cell in range(64):
            self._board[cell] = '.'

        print(self._board) 

        return self._board
    



        

    def Newboard(self)-> [[str]]:
        'Creates a new board'
        for row in range(self._row):
            self._board.append([])
            for col in range(self._column):
                self._board[-1].appends(self._none)

        return self._board


    def copyboard(self, board: [[str]])-> [[str]]:
        'Copy given game board'

        for row in range(self._row):
            self._copy.append([])
            for col in range(self._column):
                self._copy[-1].append(board[row][col])

        return self._copy
    

    def Printboard(self):
        'Takes a board and prints it as a gameboard'
        for num in range(self._column):
            print(num+1, end="   ")
        print('\n')
        for row in range(self._row):
            for col in range(self._column):
                if self._board[row][col]==self._none:
                    print('.', end = "   ")
                else:
                    print(self._board[col][row], end="   ")
            print('\n')
            

x = Board(8,8)
x.newboard()



class Move:

    def __init__(self, turn: str, move: str):
        self._turn = turn
        self._move = move
        

class Winner:
    pass
