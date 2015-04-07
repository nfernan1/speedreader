#Nicholas Fernando 12659548


import gamelogic


if __name__ == '__main__':
    

    column_size = int(input('Specify a column size:  '))
    row_size = int(input('Specify a row size: '))
    first_player = input('''Which color would you like to go first? [B]lack or [W]hite
''').upper()
    win_option = input('''[M]ost discs on board or [L]east discs on board
''').lower()



    if 4 <= column_size%2==0 <=16  or 4<= row_size%2==0 <=16:
        gs = gamelogic.Gamestate(column_size, row_size, first_player, win_option)
        gs.Board()
        print()
        print('First Turn: '+ first_player)
        print()
    else:
        raise gamelogic.InvalidColumnOrRowSize()
        print('Column and Row must be an even integer between 4 and 16')
 

        
    try:
        while gs.Game_over() == False:
            gs.Score()
            print()
            gs.Printboard()
            print('Type a digit between 0-'+ str(column_size-1)+' for a column.')
            move4 = int(input('col: '))
            print()
            print('Type a digit between 0-'+ str(column_size-1)+' for a row.')
            move3 = int(input('row: '))
            
            try:
                gs.Flip_piece(move4,move3)
                print(gs.Possible_move_list())
                gs.Score()
                gs.gotcha(move4,move3)
            except ValueError:
                print('Try Again.')
                
    except TypeError:
        print('InvalidColumnOrRow')

    finally:
        gs.Score()
        gs.How_to_win(win_option)



