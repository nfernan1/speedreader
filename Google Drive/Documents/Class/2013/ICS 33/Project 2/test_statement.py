#Nicholas Fernando 12659548
from itertools import *
from collections import deque

#store statements in a list which would give you line numbers
    #^the first element should be NONE

            

class Parser:
    def __init__(self):
        self.statement_list = [None]
        self.label_dict = {}
        self.line_dict = {}
        

    def parse(self, states: 'List of strings'):
        
        for position, element in enumerate(states):
            commands = element.split()
            self.line_dict[position+1] = element.split()
            
            if commands[0].endswith(':'):
                self.label_dict[commands[0]] = position 
                commands.pop(position)
                
            if commands[0] == 'LET':
                self.statement_list.append(LetStatement(commands[1], commands[2]))
            elif commands[0] == 'PRINT':
                self.statement_list.append(PrintStatement(commands[1]))
            elif commands[0] == 'ADD':
                self.statement_list.append(AddStatement(commands[1], commands[2]))
            elif commands[0] == 'SUB':
                self.statement_list.append(SubStatement(commands[1],commands[2]))
            elif commands[0] == 'MULT':
                self.statement_list.append(MultStatement(commands[1], commands[2]))
            elif commands[0] == 'DIV':
                self.statement_list.append(DivStatement(commands[1], commands[2]))
            elif commands[0] == 'IF':
                self.statement_list.append(IfStatement(commands[1],commands[2],commands[3],commands[4]))
            elif commands[0] == 'GOTO':
                self.statement_list.append(GoToStatement(int(commands[1])))
            elif commands[0] == 'GOSUB':
                self.statement_list.append(GoSubStatement(int(commands[1])))
            elif commands[0] == 'RETURN':
                self.statement_list.append(ReturnStatement(commands[0]))
            elif commands[0] in ('END','.'):
                self.statement_list.append(EndStatement(commands[0]))
            
                
        
        return Programstate(self.statement_list, self.label_dict, self.line_dict)
       

    
class Programstate:
    def __init__(self, statement_list, label_dict,line_dict):
        self.counter = 1
        self.variable_dict = {}
        self.statement_list = statement_list
        self.label_dict = label_dict
        self.end = True
        self.line_dict = line_dict

        
        self.gosubs = None

        
        self.stat = list(self.line_dict.keys())
        
        self.line = self.stat[self.counter]
        self.instr = self.line_dict[self.line]



    def __repr__(self):
        return'PC:{} SL: {} Vd: {} Ld:{} Line:{} '.format(self.counter,self.statement_list, self.variable_dict, self.label_dict, self.line_dict)
        

    def Get_statement_list(self):
        return self.statement_list

    
    def Get_value(self, variable, value):
        self.variable_dict[variable] = value

        
    def Get_variable(self, key):
        if key not in self.variable_dict:
            return 0
        else:
            value = self.variable_dict[key]
            return int(value)
        
        
    def Get_current_statement(self):
        return self.statement_list[self.counter]


    def rotate(self, line):

        self.counter =  line
        self.statement_list[self.counter]

    def rem_rotate(self, line):
        newline = self.instr[1]
        
        
    def Go_back(self):
        pass
        

    def Program_counter(self):
        'where I am in the program'
        self.counter += 1
        

            
        

class Statement:

    def Trace(self, programstate):
        for position, stmt in enumerate(programstate.Get_statement_list()):
                print('|||   {}| {}'.format(position, stmt))


class LetStatement:
    'Changes the value of the variable var to the given value'
                
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    
    def __repr__(self):
        return 'LET {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        programstate.Program_counter()
        programstate.Get_value(self.variable, self.value)
        print(programstate)
        return programstate
        


class PrintStatement:
    'Prints the given value to the console'
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'PRINT {}'.format(self.value)

    def execute(self, programstate: 'Programstate'):
        programstate.Program_counter()

        result = programstate.Get_variable(self.value)
        print(result)

        return programstate


class AddStatement:
    'Adds the given value to the value of the variable var'
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return 'ADD {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        programstate.Program_counter()
        newvalue = programstate.Get_variable(self.variable) + int(self.value)
        programstate.Get_value(self.variable, newvalue)
        return programstate

    

class SubStatement:
    'Subtracts the given value to the value of the variable var'
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return 'SUB {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        programstate.Program_counter()
        newvalue = programstate.Get_variable(self.variable) - int(self.value)
        programstate.Get_value(self.variable, newvalue)
        return programstate


class MultStatement:
    'Multiplies the given value to the value of the variable var'
    def __init__(self,variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return 'MULT {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        programstate.Program_counter()
        if self.value in programstate.variable_dict.keys():
            newv = programstate.Get_variable(self.variable) * programstate.Get_variable(self.value)
            programstate.Get_value(self.variable, newv)
        else:
            newvalue = programstate.Get_variable(self.variable) * int(self.value)
            programstate.Get_value(self.variable, newvalue)
        return programstate


class DivStatement:
    'Divides the given value to the value of the variable var'
    def __init__(self,variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return 'DIV {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        try:
            programstate.Program_counter()
            if self.value in programstate.variable_dict.keys():
                newv = programstate.Get_variable(self.variable) * programstate.Get_variable(self.value)
                programstate.Get_value(self.variable, newv)
            else:
                newvalue = programstate.Get_variable(self.variable) * int(self.value)
                programstate.Get_value(self.variable, newvalue)
            return programstate

        except ZeroDivisionError:
            print('Cannot Divide by 0.')
    
class GoToStatement:
    'Jumps execution of the program to the given line'
    def __init__(self, linenumber):
        self.linenumber = linenumber

    def __repr__(self):
        return 'GOTO {}'.format(self.linenumber)

    def execute(self, programstate):
        programstate.Program_counter()
        newline = self.linenumber
        programstate.rotate(newline)
        return programstate       



class IfStatement:
    'Compares the value value1 to the value value2 using the relational operator'
    def __init__(self,operator, value1, value2, line):
        self.value1 = value1
        self.value2 = value2
        self.operator = operator
        self.line = line

    def __repr__(self):
        return 'IF {} {} {} THEN {}'.format(self.value1, self.operator,self.value2, self.line)

    def execute(self, programstate: 'Programstate'):
        programstate.Program_counter()
        return programstate

class ReturnStatement:
    'Jumps execution of the program back to the line following the most recently-executed GOSUB statement'
    def __init__(self, ret):
        self.return_statement = ret

    def __repr__(self):
        return 'RETURN'

    def execute(self, programstate):
        programstate.Program_counter()
        programstate.rotate(programstate.gosubs)
        programstate.gosubs +=1
        return programstate


class GoSubStatement:
    'Temporarily jumps to the given line (which will be specified as either a line number or a label)'
    def __init__(self, linenumber):
        self.linenumber = linenumber

    def __repr__(self):
        return 'GOSUB {}'.format(self.linenumber)

    def execute(self, programstate):
        programstate.Program_counter()
        newline = self.linenumber
        programstate.gosubs = (int(programstate.stat[(programstate.counter)-2]))
        programstate.rotate(newline)
        return programstate


class EndStatement:
    'Ends the program immediately.'
    def __init__(self, end):
        self.end = end
        
    def __repr__(self):
        if self.end == 'END':
            return '{}'.format('END')
        elif self.end == '.':
            return '{}'.format('.')
    
    def execute(self, programstate: 'programstate'):
        programstate.Program_counter()
        programstate.end = False






















