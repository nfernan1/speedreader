import socketfunctions
import connectfour
import similarfxns


def _ask_for_username() -> str:
    '''
    Asks the user to enter a username and returns it as a string. Removes
    spaces inbetween usernames
    '''
    while True:
        try:
            username = input('Username: ')
            u_name = username.replace(' ', '')
            return u_name
        except:
            print('Input a username without spaces; please try again')
            
def _handle_send_command(connection: socketfunctions.SocketInfo) -> None:
    '''
    Handles a Send command by asking the user what message they'd like to
    send, then sending it to the server.
    '''
    command = input('DROP|POP: Column number: ').strip()

    if  len(command) != 0:
        command = command.split()
    else:
        if socketfunctions.send(connection, command):
            print('OKAY')
            



def _run_user_interface() -> None:
    '''
    Runs the console-mode user interface from start to finish.
    '''
    gs = connectfour.new_game_state()
    

    address = str(input("Enter the Host: "))
    port = int(input("Enter the Port ID: "))
    username = _ask_for_username()

    connection = socketfunctions.connect(address, port)

    try:
        if socketfunctions.login(connection,username):
            print("Connection Successful")
            print("WELCOME " + username)
            print("\n")
        else:
            print("Connection Failed")

        if socketfunctions.request_a_game(connection):
            print('READY')
            
        similarfxns.printboard(gs.board)
        
        while connectfour.winning_player(gs) == connectfour.NONE:
            if gs.turn == connectfour.RED:
                command = input("DROP|POP: Column number: ").strip().upper()
                print("\n")

                if len(command) == 0 or len(command.split()) < 2:
                    continue
                else:
                    command = command.split()                   
                    
                if command[0].upper() == "DROP":
                    socketfunctions.send_move(connection, str(command[0]+command[1]))
                    gs = connectfour.drop_piece(gs,int(command[1])-1)
                    similarfxns.printboard(gs.board)
                    print("OKAY")
                    print(gs.turn)
                    print(socketfunctions.SocketInfo.socket_input)
                    print(socketfunctions.SocketInfo.socket_output)
                    
                elif command[0].upper() == "POP":
                    socketfunctions.send_move(connection, str(command[0]+command[1]))
                    gs = connectfour.pop_piece(gs, int(command[1])-1)
                    similarfxns.printboard(gs.board)
                    print("OKAY")
                    
            elif gs.turn == connectfour.YELLOW:
                socketfunctions.ai_moves(connection)
 
           
    finally:
        socketfunctions.close(connection)

        
##    print("Winner: " + connectfour.winning_player(gs))


_run_user_interface()




"""
######################################


def _run_user_interface() -> None:
    '''
    Runs the console-mode user interface from start to finish.
    '''
    _show_welcome_banner()
    username = _ask_for_username()

    connection = yackety_protocol.connect(YACKETY_HOST, YACKETY_PORT)

    try:
        if yackety_protocol.login(connection, username):
            print('Welcome!')
        else:
            print('Login failed')

        # Notice how _handle_command returns False only when there are
        # no more commands to be processed.  That gives us the ability
        # to get out of this loop.
        while _handle_command(connection):
            pass

    finally:
        # No matter what, let's make sure we close the Yackety connection
        # when we're done with it.
        yackety_protocol.close(connection)



def _handle_command(connection: yackety_protocol.YacketyConnection) -> bool:
    '''
    Handles a single command from the user, by asking the user what command
    they'd like to execute and then handling it.  Returns True if additional
    commands should be processed after this one, False otherwise.
    '''
    command = input('[S]end, [L]ast, or [G]oodbye? ').strip().upper()

    if command == 'S':
        _handle_send_command(connection)
        return True
    elif command == 'L':
        _handle_last_command(connection)
        return True
    elif command == 'G':
        _handle_goodbye_command(connection)
        return False
    else:
        print('Invalid command; try again')
        return True



def _handle_send_command(connection: yackety_protocol.YacketyConnection) -> None:
    '''
    Handles a Send command by asking the user what message they'd like to
    send, then sending it to the server.
    '''
    message_to_send = input('Message to Send: ').strip()

    if len(message_to_send) == 0:
        print('Empty messages are not allowed')
    else:
        if yackety_protocol.send(connection, message_to_send):
            print('Succeeded')
        else:
            print('Failed')



def _handle_last_command(connection: yackety_protocol.YacketyConnection) -> None:
    '''
    Handles a Last command by asking the user how many messages they'd like to
    see, then asking the user to send back those messages.  The number of
    messages must be a positive number.
    '''
    try:
        how_many_messages = int(input('How many messages would you like to see? '))

    except ValueError:
        # This code will be reached if the user enters a non-number when asked
        # how many messages they'd like to see.
        print('Invalid number of messages; not a number')
        return

    if how_many_messages < 1:
        print('Invalid number of messages; must be positive')
    else:
        messages = yackety_protocol.last(connection, how_many_messages)

        # This chunk of code, in a nutshell, is why the YacketyMessage
        # namedtuple from the yackety_protocol module is so useful.
        # By getting back objects that have a "username" and a "text"
        # field, printing the messages is much more natural than it would
        # be if, for example, we had to parse the username and separate
        # it from the text here.

        print('{} message(s) found'.format(len(messages)))

        for message in messages:
            print(message.username)
            print('    ' + message.text)
            print()


if __name__ == '__main__':
    _run_user_interface()
"""
