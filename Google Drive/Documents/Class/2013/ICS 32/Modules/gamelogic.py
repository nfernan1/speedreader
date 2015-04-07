#Nicholas Fernando 12659548


class InvalidMove(Exception):
    '''Raised whenever an invalid move'''
    pass

class InvalidColumnOrRowSize(Exception):
    '''Raised whenever an invalid board size'''
    pass

class InvalidColumnOrRow(Exception):
    '''Raised whenever a column and row are not in bounds 0-7'''
    pass
    
class Gamestate:

    def __init__(self, col: int, row: int, participant:str, winning_method: str):
            
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

        self.Board()
        self.Printboard()
   


    def Board(self): 
        '''Creates new game board as a [[str]]'''

        for col in range(self._column):
            self._board.append([])

            for row in range(self._row):
                self._board[-1].append(self._empty)
                
        self._board[int(self._column/2)][int((self._row/2)-1)] += (self._black) 
        self._board[int((self._column/2)-1)][int(self._row/2)] += (self._black)
        self._board[int(self._column/2)][int(self._row/2)] += (self._white)
        self._board[int((self._column/2)-1)][int((self._row/2)-1)] += (self._white)
        self._board[3][1] += self._white
        self._board[3][0] += self._black
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
    

    def Flip_piece(self, col_num, row_num):
        '''Flips pieces if it's a valid space'''

        empty_space = self._find_empty_space()

        flippiece = self.Validate_space(col_num, row_num)

        
        if empty_space == -1:
            raise InvalidMove()

        
        else: 
            new_board = self._copy_board(self._board)
            new_board[col_num][row_num] = self._player
            for cell in flippiece:
                if new_board[cell[0]][cell[1]] == self._player:
                    new_board[cell[0]][cell[1]] = self._opposite(self._player)
                elif new_board[cell[0]][cell[1]] == self._opposite(self._player):
                    new_board[cell[0]][cell[1]] = self._player
    

                self._player = self._opposite(self._player)
        
                print()
                print('Turn: '+ self._player)
                print()
                self._board = new_board
                return self._board, self._player


    def Validate_space(self, col_num: int, row_num: int): 
        '''Validates a space on the board to flip'''
        
        surroundingcells = [[-1,1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,-1],[-1,0]]

        flippiece = []

        if self._board[col_num][row_num] != self._empty or not self._column_and_row_on_board(col_num,row_num):
            return False

        for cell in surroundingcells:

            vcol = cell[0] + col_num
            vrow = cell[1] + row_num


            if self._column_and_row_on_board(vcol,vrow) and self._board[vcol][vrow]==self._opposite(self._player):
                
                vcol += cell[0]
                vrow += cell[1]

                if not self._column_and_row_on_board(vcol,vrow):
                    continue

                while self._board[vcol][vrow]==self._opposite(self._player):
                    vcol += cell[0]
                    vrow += cell[1]

                    if not self._column_and_row_on_board(vcol,vrow):
                        break

                if not self._column_and_row_on_board(vcol,vrow):
                        continue

                
                if self._board[vcol][vrow]==self._player:
                    while True:
                        vcol -= cell[0]
                        vrow -= cell[1]

                        if vcol == col_num and vrow == row_num:
                            break
                    
                        flippiece.append([vcol,vrow])

        if flippiece==[]:
            return False

   
        return flippiece

    def Possible_move_list(self):
        '''Returns a list of all possible moves'''

        possiblemoves = []


        for col in range(self._column):
            for row in range(self._row):
                if self.Validate_space(col,row) != False and self.Validate_space(col,row) != self._player:
                    possiblemoves.append((col,row))

        return possiblemoves

    def Game_over(self):
        '''If no possible moves current player passes or game ends'''

        legalmoves = self.Possible_move_list()

        if legalmoves == []:
            return True
        else:
            return False
        
            



                              
    def gotcha(self, col_num:int, row_num:int):
        '''If no possible moves current player passes or game ends'''

        legalmoves = self.Possible_move_list()

        if legalmoves == []:
            if not self.Validate_space(col_num,row_num):
                return self.How_to_win(self._winning_method)


            return self.Flip_piece(col_num,row_num)
            
        


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
    

        print('SCORE: Black: {} White: {}'.format(self.scoreBl, self.scoreWl))
        print()
        
        
    def How_to_win(self, specify:str):
        'Specifies how the winner want to win'
    
        if self._winning_method == 'm':
            self._most_discs_win(self.scoreBl,self.scoreWl)
            
        elif self._winning_method == 'l':
            self._least_discs_win(self.scoreBl,self.scoreWl)


    def _most_discs_win(self, black_disc:int, white_disc: int):
        '''Most amount of discs on the board equals the victor'''

        if black_disc > white_disc:
            print('WINNER BLACK')
        elif white_disc > black_disc:
            print('WINNER WHITE')
        else:
            print('TIE')
            

    def _least_discs_win(self,black_disc:int, white_disc:int):
        '''Least amount of discs on the board equals the victor'''

        if black_disc < white_disc:
            print('WINNER BLACK')
        elif white_disc < black_disc:
            print('WINNER WHITE')
        else:
            print('TIE')




