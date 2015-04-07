def EnterColumn():
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
    try:
        player = input('Would you like to be: [B]lack or [W]hite ').upper()
        while not player == 'B' or player == 'W':
            print('Invalid player choice')
            player = input('Would you like to be: [B]lack or [W]hite ').upper()
        if player == 'B':
            return 'B'
        else:
            return 'W'
                       
    except NameError:
        print('Invalid player choice')
        

def Enterwinningmethod():
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
