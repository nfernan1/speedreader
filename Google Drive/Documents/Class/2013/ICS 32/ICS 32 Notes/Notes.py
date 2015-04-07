#lecture 4/23
#code from last lecture
"""
def run_user_interface():
    show_welcome_banner()

    username = ask_for_username()

    connection = yackety_protocol.connect(Yackety_host, Yackety_host)

    try:
        if yackety_protocol.login(connection, username):
            print(welcome)
        else:
            print('login failed')
        while handle_command(connection):
            pass
            
    finally:
        yackety_protocol.goodbye(connection)



def handle_command(connection: yackety_protocol.YacketyConnection)->None:
    send_or_last = input('[S]end or [L]ast ').strip().upper()

    if send_or_last == 'S':
        handle_send_command(connection)
    elif send_or_last == 'L':
        handle_last_command(connection)
    elif send_or_last == "G":
        handle_goodbye_command(connection)
    else:
        print('Invalid command; try again')




        

##def send(connection: YacketyConnection, message:str)-> bool:
##    
##    _write_line(connection,'Yackety_send ' = message)
##    return _expect_line(connection, 'Yackety_SENT')
##
####




def handle_send_command(connection: yackety_protocol.YacketyConnection)-> None:
    message_to_send = input('Message to send: ').strip()

    if len(message_to_send) == 0:
        print('Empty message arent allowed')
    else:
        if yackety_protocol.send(connection, message_to_send):
            print('succeedded')
        else:
            print('Failed')
    

def handle_last_command(connection: yackety_protocol.YacketyConnection)-> None:
    try:
        how_many_messages = int(input('How many messages would like to see? '))

        if how_many_messages < 1:
            print("Invalid numeber of messsages; must be positive")
        else:
            messages = yackety_protocol.last(connection, how_many_messages)

            for message in messages:
                print(messages.username)
                print()
            

    except ValueError:
        print("Invalid number of messages; sorry")




    

def show_welcome_banner():
    print('welcome to yackety!')
    print()
    print('please login with your username.')
    print('Remember that usernames must begin with an @ symbol')
    print()

    

def ask_for_username():
    while True:
        username = input('login: ')

        if username.startswith('@') and len(username) > 1:
            return username
        else:
            print('That username doesnt start with an @ symbol; please try again')
""


# Lecture 4/25

def square(n:int)-> int:
    return n*n

print(square(3))

class VerySimple:

    pass 
    
int('3')

str()

c

v.name


import math

# lecture 5/6

s = 3
s + 2


class X:

        def upper(self):
            return 12



s = X()
s.upper()

#DUCK TYPING

class square:
    def calculate(self, n)->float:
        return n * n


class Double:
    def calculate(self, n)->float:
        return n*2

class SquareRoot:
    def calculate(self, n):
        return math.sqrt(n)

x.calculate(9.0) #which calculate gets called? it depends on what x equals

def run_calculate(x: 'something that can calculate' , n):
    return x.calculate(n)

run_calculate(square(), 3) #function doesnt care whawt type it is

        

#lecture 5/9
# Syntatic Sugar!

def print_file_contents(file_path: str)-> None:
        file = None

        try:
                for line in file:
                        print(line[:-1])
        finally:
                if f!= None:

                        file.close()
                                

def print_file_contents(file_path: str)-> None:
        with open(file_path, 'r') as file:
                for line in file:
                        print(line[:1])

#use a with statement in the htttpResponse
                        

class MyKindOfObject:
    def __init__(self):
        print('Initializing the object') 

    def __enter__(self):
        print('Entering the context')
        return self

    # type, value, and traceback are None if no exception was raised
    # inside the "with". If an exception was raised and not caught,
    # they specify information about that exception.
    
    def __exit__(self, type, value, traceback):
        print('Exiting the context ', end='')

        if type != None:
            print('because of an exception of type {}'.format(type))
        else:
            print9'normally')

    
 """
import tkinter

def on_hello_pressed():
    print('hello')

def on_mouse_entered_hello(event: 'event object'):
    event.widget['background'] = '#00FF00'

def on_mouse_left_hello(event: 'event object'):
    event.widget['background'] = '#FF0000'
    

# on_hello_pressed() -> calls the function, its result
# on_hello_pressed -> get back the function


if __name__ == '__main__':
    root_window = tkinter.Tk()
    
    #button's are widgets #Widgets have options
     
    hello_button = tkinter.Button(
        master = root_window, text = 'Hello!', font = {'Helvetica',32},
        background = 'red',command = on_hello_pressed)
    
    # tikinter widgets generate "events"
    hello_button.bind('<Enter>', on_mouse_entered_hello)
    hello_button.bind('<Leave>', on_mouse_left_hello)

    # layout: where things go and how that changes as the size of the window
    # changes

    # one kind of layout manager is called "pack"
    hello_button.pack()
    
    root_window.mainloop()



class Counter:
    def __init__(self):
        self._count = 0

    def count(self):
        self._count +=1
        return self._count

    def reset(self):
        self._count = 0

c1 = Counter()
c2 = Counter()

##attributes belong to the object in the class                 

c1.count() #Counter.count(c1) is the same inside class Counter there's a method called count

#every method in the class takes a self


















                
