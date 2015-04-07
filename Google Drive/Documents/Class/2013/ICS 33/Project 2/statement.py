#Nicholas Fernando 12659548
from itertools import *



class Parser:
    def __init__(self):
        self.statement_list = [None]
        self.label_dict = {}
        self.line_dict = {}

        
    def parse(self, states: 'List of strings'):
        
        for position, element in enumerate(states):
            commands = element.split()
            self.line_dict[position+1] = tuple(element.split())
                        
            if commands[0].endswith(':'):
                self.label_dict[commands[0]] = position + 1
                commands.pop(position)
                
            if commands[0] == 'LET':
                self.statement_list.append(LetStatement(position+1,element,commands[1], commands[2]))               
            elif commands[0] == 'PRINT':
                self.statement_list.append(PrintStatement(position+1,element,commands[1]))
            elif commands[0] == 'ADD':
                self.statement_list.append(AddStatement(position+1,element,commands[1], commands[2]))
            elif commands[0] == 'SUB':
                self.statement_list.append(SubStatement(position+1,element,commands[1],commands[2]))
            elif commands[0] == 'MULT':
                self.statement_list.append(MultStatement(position+1,element,commands[1], commands[2]))
            elif commands[0] == 'DIV':
                self.statement_list.append(DivStatement(position+1,element,commands[1], commands[2]))
            elif commands[0] == 'IF':
                self.statement_list.append(IfStatement(position+1,element,commands[1],commands[2],commands[3],commands[5]))
            elif commands[0] == 'GOTO':
                self.statement_list.append(GoToStatement(position+1,element,int(commands[1])))
            elif commands[0] == 'GOSUB':
                self.statement_list.append(GoSubStatement(position+1,element,int(commands[1])))
            elif commands[0] == 'RETURN':
                self.statement_list.append(ReturnStatement(position+1,element,commands[0]))
            elif commands[0] in ('END','.'):
                self.statement_list.append(EndStatement(position+1,element,commands[0]))
            
                
        
        return Programstate(self.statement_list, self.label_dict, self.line_dict)
       

    
class Programstate:
    def __init__(self, statement_list: 'List of statements', label_dict,line_dict: 'Label Dictionary'):
        self.counter = 1
        self.variable_dict = {}
        self.statement_list = statement_list
        self.label_dict = label_dict
        self.end = True
        self.line_dict = line_dict
        self.gosubs = []


        

    def __repr__(self):
        'Prints the programstate dictionaries and lists'
        return'PC:{} SL: {} Vd: {} Ld:{} Line:{} '.format(self.counter,self.statement_list, self.variable_dict, self.label_dict, self.line_dict)
    

    
    def Get_value(self, variable: str, value: int):
        'Sets variable as a key and then value as a value to a corresponding key'
        self.variable_dict[variable] = value

        
    def Get_variable(self, key: str):
        'Gets the values from the variable dictionarys '
        if key not in self.variable_dict:
            return 0
        else:
            value = self.variable_dict[key]
            return int(value)
        
        
    def Get_current_statement(self):
        'Gets the current statement your program is on'
        return self.statement_list[self.counter]       

       
    def Program_counter(self):
        'where I am in the program'
        self.counter += 1
        

            
        

class Statement:

    def __init__(self,linenumbers, lineoftext):
        self.linenumbers = linenumbers
        self.lineoftext = lineoftext
        
    def Trace(self, programstate: 'Program State'):
        'take a line and print it out'
        print('||| {}| {}'.format(self.linenumbers,self.lineoftext))
        return self.execute(programstate)
        


class LetStatement(Statement):
    'Changes the value of the variable var to the given value'
                
    def __init__(self, linenumbers: int, lineoftext: str,variable: str, value: int):
        'initializes let statement global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.variable = variable
        self.value = value

    
    def __repr__(self):
        'Represents let statement object'
        return 'LET {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        'executes let statement'
        programstate.Program_counter()
        programstate.Get_value(self.variable, self.value)
        return programstate
        


class PrintStatement(Statement):
    'Prints the given value to the console'
    def __init__(self, linenumbers: int, lineoftext: str,value: str):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.value = value

    def __repr__(self):
        'Represts print statement object'
        return 'PRINT {}'.format(self.value)

    def execute(self, programstate: 'Programstate'):
        'executes print statement'
        programstate.Program_counter()

        result = programstate.Get_variable(self.value)


        return programstate


class AddStatement(Statement):
    'Adds the given value to the value of the variable var'
    def __init__(self, linenumbers: int,lineoftext: str,variable: str, value: int):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.variable = variable
        self.value = value

    def __repr__(self):
        'Represents add statement'
        return 'ADD {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        'Executes add statement'
        programstate.Program_counter()
        newvalue = programstate.Get_variable(self.variable) + int(self.value)
        programstate.Get_value(self.variable, newvalue)
        return programstate

    

class SubStatement(Statement):
    'Subtracts the given value to the value of the variable var'
    def __init__(self, linenumbers,lineoftext,variable, value):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.variable = variable
        self.value = value

    def __repr__(self):
        'Represents subtraction object'
        return 'SUB {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        'Executes substraction statement'
        programstate.Program_counter()
        newvalue = programstate.Get_variable(self.variable) - int(self.value)
        programstate.Get_value(self.variable, newvalue)
        return programstate


class MultStatement(Statement):
    'Multiplies the given value to the value of the variable var'
    def __init__(self,linenumbers,lineoftext,variable, value):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.variable = variable
        self.value = value

    def __repr__(self):
        'Represents multiplication statement'
        return 'MULT {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        'Executes multiplication statement'
        programstate.Program_counter()
        if self.value in programstate.variable_dict.keys():
            newv = programstate.Get_variable(self.variable) * programstate.Get_variable(self.value)
            programstate.Get_value(self.variable, newv)
        else:
            newvalue = programstate.Get_variable(self.variable) * int(self.value)
            programstate.Get_value(self.variable, newvalue)
        return programstate


class DivStatement(Statement):
    'Divides the given value to the value of the variable var'
    def __init__(self,linenumbers,lineoftext,variable, value):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.variable = variable
        self.value = value

    def __repr__(self):
        'Represents division statement'
        return 'DIV {} {}'.format(self.variable, self.value)

    def execute(self, programstate: 'Programstate'):
        'Executes division statement'
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
    
class GoToStatement(Statement):
    'Jumps execution of the program to the given line'
    def __init__(self, linenumbers,lineoftext,linenumber):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.linenumber = linenumber

    def __repr__(self):
        'Represents goto statement'
        return 'GOTO {}'.format(self.linenumber)

    def execute(self, programstate: 'Programstate'):
        'Executes goto statement'
        programstate.Program_counter()
        if str(self.linenumber) in programstate.label_dict.keys():
            programstate.counter = programstate.label_dict[str(self.linenumber)]
            programstate.statement_list[programstate.counter]
        else:
            programstate.counter = self.linenumber
            programstate.statement_list[programstate.counter]
        return programstate       



class IfStatement(Statement):
    'Compares the value value1 to the value value2 using the relational operator'
    def __init__(self,linenumbers,lineoftext,value1, operator, value2, line):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.value1 = value1
        self.value2 = value2
        self.operator = operator
        self.line = line

    def __repr__(self):
        'Represents if statement'
        return 'IF {} {} {} THEN {}'.format(self.value1, self.operator,self.value2, self.line)

    def execute(self, programstate: 'Programstate'):
        'Executes boolean statement with <, <=, >, >=, = (equal to), or <> (not equal to).'
        programstate.Program_counter()
        variable = programstate.Get_variable(self.value1)
        
        operators = {'<=':  lambda x,y: x<=y,
                   '<':   lambda x,y: x<y,
                   '>':   lambda x,y: x>y,
                   '>=':  lambda x,y: x>=y,
                   '<>':  lambda x,y: x!=y,
                   '=':   lambda x,y: x==y }
        
        if operators[self.operator]((variable),(int(self.value2))) == True:
            programstate.counter = int(self.line)
            programstate.statement_list[programstate.counter]
        return programstate

class ReturnStatement(Statement):
    'Jumps execution of the program back to the line following the most recently-executed GOSUB statement'
    def __init__(self, linenumbers,lineoftext, ret):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.return_statement = ret

    def __repr__(self):
        'Represents return statement'
        return 'RETURN'

    def execute(self, programstate):
        'Executes return statement'
        programstate.Program_counter()
        a = programstate.gosubs.pop()
        programstate.counter = a+1
        programstate.statement_list[programstate.counter]
        return programstate


class GoSubStatement(Statement):
    'Temporarily jumps to the given line (which will be specified as either a line number or a label)'
    def __init__(self, linenumbers,lineoftext,linenumber):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.linenumber = linenumber

    def __repr__(self):
        'Represents gosub statement'
        return 'GOSUB {}'.format(self.linenumber)

    def execute(self, programstate):
        'Executes gosub statement'
        programstate.Program_counter()
        if str(self.linenumber) in programstate.label_dict.keys():
            for key, value in programstate.line_dict.items():
                if value[0] == 'GOSUB':
                    programstate.counter = programstate.label_dict[str(self.linenumber)]
                    programstate.statement_list[programstate.counter]
                    programstate.gosubs.append(key) 
        else:
            for key, value in programstate.line_dict.items():
                if value[0] == 'GOSUB':
                    programstate.counter = self.linenumber
                    programstate.statement_list[programstate.counter]
                    programstate.gosubs.append(key) 
        return programstate


class EndStatement(Statement):
    'Ends the program immediately.'
    def __init__(self, linenumbers,lineoftext,end):
        'Initializes global parameters'
        Statement.__init__(self, linenumbers, lineoftext)
        self.end = end
        
    def __repr__(self):
        'Represents end program statement'
        if self.end == 'END':
            return '{}'.format('END')
        elif self.end == '.':
            return '{}'.format('.')
    
    def execute(self, programstate: 'programstate'):
        'Ends bumpkin interpretor '
        programstate.Program_counter()
        programstate.end = False






















