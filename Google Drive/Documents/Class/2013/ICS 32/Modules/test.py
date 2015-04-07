import gamelog
import inputs


# check if the games over
# 
# which player will move first





if __name__ == '__main__':
    print('Let\'s play some Reversi!')
    

    column = inputs.EnterColumn()
    row = inputs.EnterRow()
    player = inputs.Enterplayer()
    winningmethod = inputs.Enterwinningmethod()
        

    gs = gamelog.Gamestate(column, row, player, winningmethod)


    print('First Turn: '+player)

    while True:
        if gs.Turn() == 'B':
            gs.Score()
            print('Possible moves for '+ gs.Turn())
            print(gs.Possible_move_list())
            print('Enter a number from 0 to '+ str(column-1))
            space = inputs.EnterPlayercolumn()
            print('Enter a number from 0 to '+ str(row-1))
            space2 = inputs.EnterPlayerrow()
            gs.Flip_piece(space, space2)
            gs.Printboard()
            if gs.Possible_move_list() == []:
                break
            else:
                print('Turn: '+gs.Turn())

        else:
            gs.Score()
            print('Possible moves for '+ gs.Turn())
            print(gs.Possible_move_list())
            print('Enter a number from 0 to '+ str(column-1))
            space = inputs.EnterPlayercolumn()
            print('Enter a number from 0 to '+ str(row-1))
            space2 = inputs.EnterPlayerrow()
            gs.Flip_piece(space, space2)
            gs.Printboard()
            if gs.Possible_move_list() == []:
                break
            else:
                print('Turn: '+gs.Turn())

    gs.Score()
    print('CONGRATULATIONS!')
    print(gs.How_to_win(winningmethod))
    
        
