import gamelog


def EnterColumn():
    '''User enters the size they want the boards columns to be'''
    try:
        col_opt = '4 6 8 10 12 14 16'.split()
        while True:
            print('Enter Column size: ')
            columnsize = input()
            
            if columnsize in col_opt:
                return int(columnsize)
            else:
                print()
                print('Invalid column size')
                print('Input an EVEN integer between 4 and 16')
                print()
                continue
        
    except ValueError:
        print('Invalid Column size')
        

def EnterRow():
    '''User enters the boards row size'''
    try:
        row_opt = '4 6 8 10 12 14 16'.split()
        while True:
            print('Enter Row size: ')
            rowsize = input()
            
            if rowsize in row_opt:
                return int(rowsize)
            else:
                print()
                print('Invalid row size')
                print('Input an EVEN integer between 4 and 16')
                print()
                continue
        
    except ValueError:
        print('Invalid row size')
        

def Enterplayer():
    '''User enters which player they would like to go first'''
    try:
        player = input('''Would you like to be: [B]lack or [W]hite
''').upper()
        while not (player == 'B' or player == 'W'):
            print('Invalid player choice')
            player = input(''''Would you like to be: [B]lack or [W]hite
''').upper()
        if player == 'B':
            print('1')
            return 'B'
        else:
            print('2')
            return 'W'
                       
    except NameError:
        print('Invalid player choice')
        
        

def Enterwinningmethod():
    ''''User chooses how they would like to win the game'''    
    try:
        winmethod = 'L M'.split()
        while True:
            print('How would you like to win: [M]ost points or [L]east points')
            move = input().upper()
            
            if move in winmethod:
                return str(move)
            else:
                print()
                print('Invalid input for winning method')
                print('Input M or L')
                print()
                continue
    except NameError:
        print('Invalid Input for winning method')


def EnterPlayercolumn():
    '''User enters the column they would like to place a piece to'''
    columnnumbers = '0 1 2 3 4 5 6 7 8 9'.split()
    columndouble = '10 11 12 13 14 15'.split()
    setofcolnumbers = (columnnumbers + columndouble)

    while True:
        space = input('Enter Column Number: ')
        if space in setofcolnumbers:
            col = int(space)
            break
        else:
            print('Not a valid Column number.')

    return int(col)




def EnterPlayerrow():
    '''User enters the row tehy would like to place a piece to'''
    rownumbers = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'.split()

    while True:
        space = input('Enter Row Number: ')
        if space in rownumbers:
            row = int(space)
            break
        else:
            print('Not a valid Row number')

    return int(row)


