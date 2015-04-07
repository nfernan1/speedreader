#Nicholas Fernando 12659548


class InvalidMove(Exception):
    '''Raised whenever an invalid move'''
    pass

class InvalidColumnsize(Exception):
    '''Raised whenever an invalid column size is specified'''
    pass

class InvalidColumnOrRowSize(Exception):
    '''Raised whenever an invalid board size'''
    pass

class InvalidColumnOrRow(Exception):
    '''Raised whenever a column and row are not in bounds 0-7'''
    pass
    
class Gamestate:

    def __init__(self, col: int, row: int, participant:str, winning_method: str, startpiece: str):
            
        self._board = []
        self._copy = []
        
        self._row = row
        self._column = col
        
        
        self._empty = ''
        self._black = 'B'
        self._white = 'W'

        
        self._winning_method = winning_method
        self.scoreBl = 0
        self.scoreWl = 0

        self._player = participant
        self._startpiece = startpiece



        
   


    def Board(self): 
        '''Creates new game board as a [[str]]'''

        for col in range(self._column):
            self._board.append([])

            for row in range(self._row):
                self._board[-1].append(self._empty)
                
        if self._startpiece == self._white:                
            self._board[int(self._column/2)][int((self._row/2)-1)] += (self._black) 
            self._board[int((self._column/2)-1)][int(self._row/2)] += (self._black)
            self._board[int(self._column/2)][int(self._row/2)] += (self._white)
            self._board[int((self._column/2)-1)][int((self._row/2)-1)] += (self._white)
        elif self._startpiece == self._black:
            self._board[int(self._column/2)][int((self._row/2)-1)] += (self._white) 
            self._board[int((self._column/2)-1)][int(self._row/2)] += (self._white)
            self._board[int(self._column/2)][int(self._row/2)] += (self._black)
            self._board[int((self._column/2)-1)][int((self._row/2)-1)] += (self._black)


        return self._board

    

    def Printboard(self): 
        '''Prints the board'''
        
        for num in range(self._column):
            print('   '+ str(num), end='')
        print('\n')

            
        for row in range(self._row):
            print(row, end='  ')
            for col in range(self._column):
                if self._board[col][row] == self._empty:
                    print('.', end='   ')
                
                else:
                    print(self._board[col][row], end='   ')

            print('\n')



    def _copy_board(self, board:[[str]]): 
        '''Copies an existing board'''
        for col in range(self._column):
            self._copy.append([])

            for row in range(self._row):
                self._copy[-1].append(board[col][row])

        return self._copy
        
        

    def _opposite(self, player: str): 
        '''return opposite player'''

        if player == self._black:
            return self._white
        else:
            return self._black
        
    def Turn(self):
        '''Specifies which player's turn it is'''
        if self._player == self._black:
            return 'Turn: Black'
        else:
            return 'Turn: White'
        

    def _find_empty_space(self): 
        '''Checks to see if a space is empty'''

        for col in range(self._column):
            for row in range(self._row):
                if self._board[col][row] == self._empty:
                    return [col,row]

        return -1
                   
    
    def _column_and_row_on_board(self, col_num: int, row_num): 
        '''Checks if move is in the the board'''
        return 0 <= col_num < self._column and 0<= row_num < self._row
    

    def Flip_piece(self, col_num:int, row_num:int):
        '''Flips pieces if it's a valid space'''

        empty_space = self._find_empty_space()

        flippiece = self.Valid_space(col_num, row_num, self._player)

        
        if flippiece == False:
            return False
        else:
            if self._player == self._player and self.Possible_move_list() != []:
                new_board = self._copy_board(self._board)
                new_board[col_num][row_num] = self._player
        
                for col,row in flippiece:
                    if new_board[col][row] == self._player:
                        new_board[col][row] = self._opposite(self._player)
                    elif new_board[col][row] == self._opposite(self._player):
                        new_board[col][row] = self._player
        

                self._player = self._opposite(self._player)
                self._board = new_board
                    
            return True




    def Valid_space(self, col_num: int, row_num: int, player: str): 
        '''Validates a space on the board to flip'''
        player = self._player
                    
        surroundingcells = [[-1,1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,-1],[-1,0]]

        flippiece = []

        if self._board[col_num][row_num] != self._empty or not self._column_and_row_on_board(col_num,row_num):
            return False

        for row,col in surroundingcells:

            vcol = col + col_num
            vrow = row + row_num


            if self._column_and_row_on_board(vcol,vrow) and self._board[vcol][vrow]==self._opposite(self._player):
                
                vcol += col
                vrow += row

                if not self._column_and_row_on_board(vcol,vrow):
                    continue

                while self._board[vcol][vrow]==self._opposite(self._player):
                    vcol += col
                    vrow += row

                    if not self._column_and_row_on_board(vcol,vrow):
                        break

                if not self._column_and_row_on_board(vcol,vrow):
                        continue

                
                if self._board[vcol][vrow]==self._player:
                    while True:
                        vcol -= col
                        vrow -= row

                        if vcol == col_num and vrow == row_num:
                            break
                    
                        flippiece.append([vcol,vrow])

        if flippiece==[]:
            return False
        else:   
            return flippiece


    def Possible_move_list(self):
        '''Returns a list of all possible moves'''

        possiblemoves = []


        for col in range(self._column):
            for row in range(self._row):
                if self.Valid_space(col,row, self._player) != False: #and self.Valid_space(col,row, self._player) != self._player:
                    possiblemoves.append([col,row])

        return possiblemoves


            
    def Score(self): 
        '''Returns count of tiles on the board'''
        self.scoreBl = 0
        self.scoreWl = 0
    
        for col in range(self._column):
            for row in range(self._row):
                if self._board[col][row] == self._black:
                    self.scoreBl += 1
                elif self._board[col][row] == self._white:
                    self.scoreWl += 1
    

        score = 'SCORE: Black: {} White: {}'.format(self.scoreBl, self.scoreWl)
        return str(score)
        


    def _win(self):
        '''Most amount of discs on the board equals the victor'''
        
        if self._winning_method == 'm':
            if self.scoreBl > self.scoreWl:
                return 'WINNER BLACK'
            elif self.scoreWl> self.scoreBl:
                return 'WINNER WHITE'
            elif self.scoreWl == self.scoreBl:
                return 'TIE: NO WINNER'
            
        elif self._winning_method == 'l':
            if self.scoreBl < self.scoreWl:
                return 'WINNER BLACK'
            elif self.scoreWl < self.scoreBl:
                return 'WINNER WHITE'
            elif self.scoreWl == self.scoreBl:
                return 'TIE: NO WINNER'

                


