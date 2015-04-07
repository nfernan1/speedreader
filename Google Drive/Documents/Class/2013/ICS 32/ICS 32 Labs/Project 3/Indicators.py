#indicators module
#Simple Moving Average
"""
an execute method that executes the strategy against a list of price quotes.
"""

#execute takes two lists one for the date and one for the closing price, so when you specify an index it runs through a loop and gets up to that range
#and prints averages the close price
#do that by parsing the file by comma sep=','
#an attribute to store the closing prices of the file
#an attribute to calculate the average

test = [570,580,590,600,590,580,570,560,570]
test2 = [1,1,1,-1,-1,-1,-1,1]
##days = int(input('How many days would you like to average? '))


class Running_average:

    def __init__(self, days: int, closing:list ):
        self._days = days
        self._closingprices = closing
        

    def average(self)->list:
        '''Takes the average of the elements of a list'''
        val = [0]*(self._days-1)
        for values in range(self._days,len(self._closingprices)):
##            print (self._closingprices[values-self._days])
##            print('hey')
##            print(self._closingprices[(values-self._days)+1])
            val.append((sum(self._closingprices[values-self._days:values]))/self._days)
        return val
        
            
            
    def execute(self, classe: 'class', indic: 'indicator',days: int,prices: list)->list:
        prices = classe(days,prices)
        print(prices.indicator())


        

##class Directional_Indicator:
##
##    def __init__(self, days:int, closing:list):
##        self._days = days
##        self._closingprices = closing
##
##    def direct(self):
##        '''Number of closing prices out of the most recent N on which the stock went up'''
##        ind = [0]
##        ica = [0]
##        
##        for  before, after in zip(self._closingprices, self._closingprices[1:]):
##            if before < after:
##                ind.append(1)
##            else:
##                ind.append(-1)
##        
##        for values in range(2,len(ind)+1):
##            if values <= self._days:
##                ica.append((sum(ind[:values])))
##
##            else:
##                ica.append((sum(ind[values-self._days:values])))
##        return ica
##
##
##    def execute(self, classe: 'class', indic: 'indicator',days: int,prices: list)->list:
##        prices = classe(days,prices)
##        print(prices.indicator())
##
####x = Directional_Indicator(days, test)
####x.direct()



