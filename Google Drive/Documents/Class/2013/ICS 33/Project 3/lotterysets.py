#Nicholas Fernando 12659548
import collections

class LotterySetError(Exception):
    'Exception class raised whenever one of the functions or methods in lotterysets fails'
    pass


def make_lottery_set_type(game_name: str, num_count: int, min_max: tuple):
    'Function that creates a lottery set object'
    'creates a new class of lottery set'
    #int: needs to be at least 1--no upper limit
    #tuple: max needs to be at least as large as minimum i.e.,(5,4) is illegal, but (1,4) isn't

    class LotterySet:
        'Creates a lottery set object'
        set_size = num_count
        min_set_number = min_max[0]
        max_set_number = min_max[1]
        
        def __init__(self, number_list: list):
            self.game_name = game_name
            self.min_max = min_max
            
            self.set_size = num_count
            self.min_set_number = min_max[0]
            self.max_set_number = min_max[1]
            
            self.number_list = self._unique_number(self._valid_index(number_list))

            self.step = 0
            self.counter = 0

        def __len__(self):
            'Returns the length of the set'
            if len(self.number_list) == self.set_size:
                return len(self.number_list)
            else:
                raise LotterySetError('Not Enough Numbers')
            
        def _valid_index(self, int_list: list):
            'Checks to see if the integers are in the objects range'
            
            for number in int_list:
                if number not in range(self.min_set_number, self.max_set_number+1):
                    raise LotterySetError('Integer Not Within Valid Range')

            return int_list

        def _unique_number(self, int_list: list):
            'Checks to see if all integers in the set are unique numbers'
            if len(int_list) != len(set(int_list)):
                raise LotterySetError('Numbers must be Unique')
            else:
                return int_list

        def full_match(self,other:'Lottery Set Class'):
            'Compares two lottery objects'
            if self.game_name == other.game_name:
                match = collections.Counter(self.number_list) == collections.Counter(other.number_list)
                return match
            else:
                raise LotterySetError('Incompatible Set Types')

        def match_count(self, other: 'Lottery Set Class'):
            'Checks to see if the integer is within the set' 
            if self.game_name == other.game_name:
                check = []
                for value in self.number_list:
                    if value in other.number_list:
                        check.append(value)
                return len(check)   
            else:
                raise LotterySetError('No Matches in Set(s)')
                
        def __eq__(self, other):
            'Operator overload for the equal operator'
            if self.game_name == other.game_name and self.set_size == other.set_size and \
               self.min_set_number == other.min_set_number and self.max_set_number == other.max_set_number and \
               sorted(self.number_list)== sorted(other.number_list):
                return True
            else:
                return False
        

        def __contains__(self, other):
            'Allows to see what elements are in the list'
            if other in self.number_list:
                return True
            else:
                return False
            
        def __next__(self):
            'Gets the next item of the list'

            if self.counter == len(self.number_list):
                raise StopIteration()
            else:
                
                self.counter+=1
                while True:
                    
                    index = self.number_list[self.step]
                    self.step +=1
                    
                    return index


        def __reversed__(self):
            'Reverses number list'
            return reversed(self.number_list)

            
        def __iter__(self):
            'Returns an iterated object set'
            return self
            
        
        def __repr__(self):
            'Canonical representation of the lottery set class'
            return "make_lottery_set_type('{}', {}, {})({})".format(self.game_name, self.set_size, self.min_max,self.number_list)

    return LotterySet


