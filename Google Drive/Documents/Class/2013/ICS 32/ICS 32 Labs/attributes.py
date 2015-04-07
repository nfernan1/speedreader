##class MyKindOfObject:
##    def __init__(self):
##        print('Initializing the object')
##
##    def __enter__(self):
##        print('Entering the context')
##        return self
##
##    # type, value, and traceback are None if no exception was raised
##    # inside the "with". If an exception was raised and not caught,
##    # they specify information about that exception.
##    
##    def __exit__(self, type, value, traceback):
##        print('Exiting the context ', end='')
##
##        if type != None:
##            print('because of an exception of type {}'.format(type))
##        else:
##            print('normally')
##
##    
##        
##def print_file_contents(file_path: str)-> None:
##    with open(file_path, 'r') as file:
##            for line in file:
##                    print(line[:1])


import socket

class HttpRequester:
    
    def __int__(self, host:str, port: int):
        self._host = host
        self._port = port

        self._socket = None
        self._socket_input = None
        self._socket_output = None

        self._socket = socket.socket()
        self._socket.connect((host, port))

        self._socket_input = self._socket.makefile('r')
        self._socket_output = self._socket.makefil('w')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        if self._socket_input != None:
            self._socket_input.close()
            self._socket_input != None

        if self._socket_output != None:
            self._socket_output.close()
            self._socket_output = None

        if self._socket != None:
            self._socket.close()
            self._socket = None

    def make_request(self, resource: str)-> None:
        self._socket_output.write('Get' + resource + 'HTTP/1.1\n')
        self._socket_output.write('Host: '+ self._host + '\n')
        self._socket_output.write('\n')
        self._socket_output.flush()

        for line in self._socket_input.readlines(): #for every line in list--produces a list
            print(line[:-1])
    

# with lets somehting have you close something for you automatically if you fall outside of a certain scope
# theres no little area to put the with statement in the class 

with HttpRequester('www.ics.uci.edu', 80) as requester:
	hello = requester.make_request('/~thornton/ics32/ProjectGuide/Project3/')
	print(hello)
