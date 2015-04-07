#Nicholas Fernando 12659548
import unittest
from statement import *

class ProgramStateTest(unittest.TestCase):

    def setUp(self):
        'Sets up the test state'
        self.ps = Programstate(statement_list = [], label_dict = {}, line_dict = {})

    def test_get_value(self):
        'Tests get value method'
        self.ps.Get_value('A', 1)
        self.assertEqual(self.ps.variable_dict, {'A':1})

    def test_get_variable(self):
        'Tests get variable method'
        valueequalszero = self.ps.Get_variable('B')
        self.assertEqual(valueequalszero, 0)
        self.ps.Get_value('A', 5)
        valueequals5 = self.ps.Get_variable('A')
        self.assertEqual(valueequals5, 5)


    def test_program_counter(self):
        'Tests program counter method'
        self.ps.Program_counter()
        self.assertEqual(self.ps.counter, 2)

        



if __name__=='__main__':
    unittest.main(exit = False) 
