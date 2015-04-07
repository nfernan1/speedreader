from collections import namedtuple
import connectfour

def printboard(board: list)->namedtuple:
    '''takes a list/the board and prints it out in gameboard format''' 
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

def ask_for_move() -> str:
    '''console will ask user to enter a move; returns the move as a string in all caps'''
    while True:
        command = input("DROP|POP: Column number: ").strip().upper()
        if len(command) == 0 or len(command.split()) < 2:
            continue
        else:
            return command

def handle_drop_command(gs: connectfour.ConnectFourGameState, col: int) -> connectfour.ConnectFourGameState:
    '''if user enters drop, returns a gamestate that reflects dropped piece'''
    if gs.board[col-1][0] != connectfour.NONE:
        print("Invalid Move.")
        print("\n")
    else:
        gs = connectfour.drop_piece(gs, col-1)
        return gs

def handle_pop_command(gs: connectfour.ConnectFourGameState, col: int) -> connectfour.ConnectFourGameState:
    '''if user enters pop, returns a gamestate that reflects popped piece'''
    if gs.board[col-1][-1] != gs.turn:
        print("Invalid Move.")
        print("\n")
    else:
        gs = connectfour.pop_piece(gs, col-1)
        return gs
