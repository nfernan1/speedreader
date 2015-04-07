import socket
import connectfour
import collections
import similarfxns

# login function
# ai-move
# put the ai-move into drop_piece and connectfour.pop_piece() functions and put it into a while loop
            


SocketInfo = collections.namedtuple(
    'SocketInfo',
    ['socket', 'socket_input', 'socket_output'])

def _read_line(connection: SocketInfo) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    return connection.socket_input.readline()[:-1]


def _expect_line(connection: SocketInfo, line_to_expect: str) -> bool:
    '''
    Reads a line of text sent from the server, expecting it to contain
    a particular text.  Returns True if the expected text was sent,
    False otherwise.
    '''
    return _read_line(connection) == line_to_expect


def _write_line(connection: SocketInfo, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence.
    '''
    connection.socket_output.write(line + '\r\n')
    connection.socket_output.flush()


def close(connection: SocketInfo) -> None:
    '''Closes the connection to the server'''
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()

def ai_moves(connection:SocketInfo):
    if _expect_line(connection, 'OKAY'):
        print("OKAY")
        if _read_line(connection)[0].upper() == "DROP":
            gs = connectfour.drop_piece(gs, int(_read_line(connection)[-1]))
            similarfxns.printboard(gs.board)
        elif _read_line(connection)[0].upper() == "POP":
            gs = connectfour.pop_piece(gs, int(_read_line(connection)[-1]))
            similarfxns.printboard(gs.board)

    elif _expect_line(connection, 'READY'):
        print("READY")
        
    elif _expect_line(connection, 'INVALID'):
        print("INVALID")
        
            
    elif _expect_line(connection, 'WINNER_RED'):
        print("WINNER_RED")
        close(connection)
    elif _expect_line(connection, 'WINNER_YELLOW'):
        print("WINNER_YELLOW")
        close(connection)


############################              

def connect(host: str, port: int):

    c4_socket = socket.socket()
    
    c4_socket.connect((host, port))

    #what we read from the namedtuple
    c4_socket_input = c4_socket.makefile('r')
    #what we write to the namedtuple
    c4_socket_output = c4_socket.makefile('w')
    
    return SocketInfo(
        socket = c4_socket,
        socket_input = c4_socket_input,
        socket_output = c4_socket_output)



def login(connection: SocketInfo, username: str) -> bool:
    '''
    Logs a user into the server over a previously-made connection,
    returning True if successful and False otherwise.
    '''
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    return _expect_line(connection, 'WELCOME ' + username) 

   

def request_a_game(connection: SocketInfo):
    print('To request a game type: AI_GAME') 
    request = input('Request a game: ').upper()
    _write_line(connection, request)
    return _expect_line(connection, 'READY')



def send_move(connection: SocketInfo, move: str):
    _write_line(connection, move)
    return _expect_line(connection,'OKAY')





