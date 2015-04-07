from collections import namedtuple
import connectfour

def printboard(board: list)->namedtuple:
    for num in range(connectfour.BOARD_COLUMNS):
        print(num+1, end="   ")
    print("\n")
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if board[col][row]== connectfour.NONE:
                print(".", end = "   ")
            else:
                print(board[col][row], end ="   ")
        print("\n")
       



#When use pop on invalid move should print "invalid move" and reiterate
#through the while loop again
#^same for entering an "empty string"        

def action_options():
    gs = connectfour.new_game_state()
    print("Place a space between your action and number.")
    print("\n")
    
    while connectfour.winning_player(gs)== connectfour.NONE:
        command = input("DROP|POP: Column number: ").strip()
        
        if len(command) == 0:
            continue
        else:
            command = command.split()
        
        if command[0].lower() == "drop":
            print("\n")
            
            if gs.board[int(command[1])-1][0] != connectfour.NONE:
                print("Invalid Move.")
                print("\n")
            else:
                gs = connectfour.drop_piece(gs, int(command[1])-1)
                printboard(gs.board)
            
        elif command[0].lower() == "pop":
            print("\n")
            
            if gs.board[int(command[1])-1][-1] != gs.turn:
                print("Invalid Move.")
                print("\n")
            else:
                gs = connectfour.pop_piece(gs, int(command[1])-1)
                printboard(gs.board)
        
                        
    print("Winner: " + connectfour.winning_player(gs))





