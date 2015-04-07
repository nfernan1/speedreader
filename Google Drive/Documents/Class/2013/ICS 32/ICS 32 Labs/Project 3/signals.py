import Indicators

"""
Generate buy and sell signals based on the N-day simple moving average, with the user
choosing N (i.e., the number of days). Smaller numbers of days are more
sensitive (i.e., more likely to generate a signal),
while larger numbers of days are less so. Signals are generated as follows:

If the closing price on a particular day has crossed above the
simple moving average

the closing price on that day is above that day's simple moving average,
while the previous closing price is not above the previous simple moving average

generate a buy signal.

If the closing price on a particular day has crossed
below the simple moving average, generate a sell signal.
Otherwise, generate no signal.
"""

def reverse(a: list)->list:
    rl = []
    for i in a:
        rl.append(i)
    return rl

tests = [570,580,590,600,590,580,570,560,570]
test = reverse(tests)

temp = [0,0,580.00,590.00,593.33,590.00,580.00,570.00,567.67]
days = int(input('How many days would you like to average? '))




class SMAsignal:

    def __init__(self, day: int, sma: list, rent: list):
        self._rent = rent
        self._smal = sma
        self._day = day



    def signals(self):
        sig = []
        for values in range(len(self._smal)):
            if self._smal[(values-self._day)-6] > self._rent[(values-self._day)] and self._smal[(values-self._day)-5] < self._rent[(values-self._day)+3]:
                sig.append('Sell')
            elif self._smal[(values-self._day)-5] < self._rent[(values-self._day)] and self._smal[(values-self._day)-5] > self._rent[(values-self._day)+3]:
                sig.append('Buy')
            else:
                sig.append('')
        print(sig)
        return sig


    def execution(self):
        pass


ind = [0,1,2,5,3,2,1,-1,-3,-3]
print(ind)

"""
Generate buy and sell signals based on the N-day directional indicator,
with the user choosing N (i.e., the number of days) and buy and sell thresholds.
If the directional indicator has crossed above the buy threshold
(i.e., the indicator above the buy threshold on that day but is not above
the buy threshold on the previous day),
generate a buy signal.
If the directional indicator has crossed
below the sell threshold, generate a sell signal.
Otherwise, generate no signal.
"""
buy = int(input('Buy threshold: '))
sell = int(input('Sell threshold: '))

class DIsignal:

    def __init__(self, day: int, dil: list, buy: int, sell: int):
        self._dil = dil
        self._day = day
        self._buy = buy
        self._sell = sell


    def dignal(self):
        dig = []
        for values in range(len(self._dil)):
            if self._dil[values] > self._buy:
                dig.append('Buy')
            elif self._dil[(values)-1] <= self._buy:
                dig.append('')
            print(self._dil[values])
            print()
            print(dig)



##            if self._dil[(values-self._day)+5] > self._buy:
##                dig.append('Buy')
##            elif self._dil[(values-self._day)+5] < self._sell:
##                dig.append('Sell')
##            elif self._dil[(values-self._day)+6] >= self._dil[(values-self._day)+5]:
##                dig.append('')
##            
##
##            print(self._dil[(values-self._day)+5])


x = DIsignal(days, ind, buy, sell)

x.dignal()
