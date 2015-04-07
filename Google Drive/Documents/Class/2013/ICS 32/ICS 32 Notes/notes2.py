YacketyConnection = collections.namedtuple('YacketyConnection', ['socket','socket_input','socket_output'])

def connect(host, port)-> YacketyConnection:
    yackety_socket = socket.socket()
    yackety_socket.connect((host, port))

    yackety_socket_input = yackety_socket.makefile('r')
    yackety_socket_output = yackety_socket.makefile('w')
    return YacketyConnection(socket = yackety_socket,
                             socket_input = yackety_socket_input
                             socket_output = yackety_socket_output)

def login(conncetion, username):
    _write_line(connection, "Yackety_Hello" + username)
    return _expect_line(connection, "Yackety_hello")

def last(connection, how_many_messages):
    _write_line(connection, "Yackety_last {}".format(how_many_messages))

    messages = []

    message_count_line = _read_line(connection)

    if message_count_line.startswith('YACKETY_MESSAGE_COUNT'):
        number_of_messages = int(message_count_line[22:])

        for i in range(number_of_messages):
            message_line = _read_line(connection)

            if message_line.startswith('YACKETY_MESSAGE'):
                message_words = message_line.split()

                username = message_words[1]
                text_start = 17 + len(username)
                text = message_line[text_start:]
                messages.append(Yackety_Message_count, text)
            
        

    return messages

def goodbye(connection):
    _write_line("")
    _expect_line("")
    -good()

def _read_line(connection):
    return connection.socket_input.readline()[:1]

def _write_line(conenction, line):
    connection.socket_output.write(line +"\r\n")
    conenction.socket_output.flush()

def _ecpect_line(connection, line_to_ecpect):
    line_received = connection.socket_input.readline()[:1]
    return line_received == line_to_ecpect

def goodbye(connection: YacketyConnection):
    socket.close()
