import random
import json
import csv
from decimal import Decimal

##def ccinfofile():
##    'Opens a file at the start of the program and writes everything to it'
##    exact = True
##
##    while exact:
##        command = input('input: '+'\n')
##        with open('ccinfo.txt', 'a') as c:
         

class Currency:

    def __init__(self):
        self._base_rate = {}



    def readfile(self):

        
        with open('currency.txt') as currency:
            cur = currency.read()
            cur_split = cur.splitlines()

        return cur_split
    

    def er_dict(self):
        
        self.indicnames = []
        self.exchangerate = []
        
        for indicator in self.readfile():
            self.indicnames.append(indicator[0:3])
            self.exchangerate.append(indicator[6:12])

            self._exchange_dict = dict(zip(self.indicnames, self.exchangerate))

                     
        return self._exchange_dict
    

    def combo_dict(self):

        self.exchangerate = []
        self.decimalplaces = []

        for indicator in self.readfile():
            self.exchangerate.append(indicator[6:12])
            self.decimalplaces.append(indicator[4:5])

            self._combo = dict(zip(self.exchangerate,self.decimalplaces))

        return self._combo
    

    def baseline(self):
        
        return self.readfile()[0][6:12]


    def decimal_placement(self, num: str):

        for value in self.combo_dict():
            if value == num: #value is a string
                decimal = self.combo_dict()[value]
                if decimal == '0':
                    return Decimal(value).quantize(Decimal(decimal)) #string
                else:
                    return Decimal(value).quantize(Decimal(str(.11*int(decimal)))) #string
                
        
    def baseline_conversion(self, currencycode:str, amount: str):
        'Converts currency to baseline currency'
        for indic in self.er_dict():
            if indic == currencycode:
                exchangerate = self.decimal_placement(self.er_dict()[currencycode])
                convertedtobase = (self.decimal_placement(self.baseline())/ exchangerate) * Decimal(amount)
                
                if self.combo_dict()[self.baseline()] == '0':
                    correctdecimal = Decimal(convertedtobase).quantize(Decimal(str(1)))
                elif self.combo_dict()[self.baseline()] == '1':
                    correctdecimal = Decimal(convertedtobase).quantize(Decimal(str(.1)))
                elif self.combo_dict()[self.baseline()] == '2':
                    correctdecimal = Decimal(convertedtobase).quantize(Decimal(str(.11)))


                return correctdecimal
            

    def convertback(self, currencycode: str, amount: str):
        'Converts the currency back to original currency'

        for indic in self.er_dict():
            if indic == currencycode:
                exchangerate = self.decimal_placement(self.er_dict()[currencycode])
                convertedtooriginal = ((Decimal(amount)*Decimal(exchangerate))/(self.decimal_placement(self.baseline())))
                
                if self.combo_dict()[self.baseline()] == '0':
                    correctdecimal = Decimal(convertedtooriginal).quantize(Decimal(str(1)))
                elif self.combo_dict()[self.baseline()] == '1':
                    correctdecimal = Decimal(convertedtooriginal).quantize(Decimal(str(.1)))
                elif self.combo_dict()[self.baseline()] == '2':
                    correctdecimal = Decimal(convertedtooriginal).quantize(Decimal(str(.11)))


                return correctdecimal


                                      
                                       

class Money:

    def __init__(self, currencycode, money):

        self.currencycode = currencycode
        self.money = money
        self.mon = money
  

        self.CC = Currency()

    def getmoney(self):
        return self.money
    

    def __eq__(self, other):
        return self.CC.baseline_conversion(self.currencycode, self.money) == self.CC.baseline_conversion(other.currencycode, other.money)
                                                    
                                                    
    def __lt__(self, other):
        print(type(other))
        return self.CC.baseline_conversion(self.currencycode, self.money) < self.CC.baseline_conversion(other.currencycode, other.money)
        
    def __le__(self,other):
        return self.CC.baseline_conversion(self.currencycode, self.money) <= self.CC.baseline_conversion(other.currencycode, other.money)
    

    def __gt__(self,other):
        return self.CC.baseline_conversion(self.currencycode, self.money) > self.CC.baseline_conversion(other.currencycode, other.money)
    

    def __ge__(self,other):
        return self.CC.baseline_conversion(self.currencycode, self.money) >= self.CC.baseline_conversion(other.currencycode, other.money)


    def __add__(self,other):
        
        self.money = self.CC.baseline_conversion(self.currencycode, self.money) + self.CC.baseline_conversion(other.currencycode,other.money)
        return self.CC.convertback(self.currencycode,self.money)
        
        
    def __sub__(self,other):

        self.money = self.CC.baseline_conversion(self.currencycode, self.mon) - self.CC.baseline_conversion(other.currencycode, other.mon)
        return self.CC.convertback(self.currencycode,self.money)
         


    def __repr__(self):
        return '{}'.format(self.money)

    


class Credit_card:
    
    def __init__(self, currencycode: str, balance: 'Money Object', limit:'Money Object'):

        self.currencycode = currencycode
        
        self.limit = limit
        self.balance = balance

        
    def __repr__(self):

        return '{} {} {}'.format(self.currencycode, self.balance, self.limit)

    def getbalance(self):
        return self.balance

    def getcurrencycode(self):
        return self.currencycode

    
    def getlimit(self):
        return self.limit


    def purchase(self, amount:'Money Object'):
        if self.balance > self.limit:
            print('OVER_LIMIT')
        else:
            print(type(self.limit))
            self.balance + amount

    def payment(self, amount: 'Money Object'):
        if self.balance - amount < self.balance:
            print('NONPOSITIVE_AMOUNT')
        else:
            self.balance - amount


    
    def GenerateCard(self):
        'Generates a unique random 5-digit integer'
        self.cardnum = random.randint(10000, 99999)
        return self.cardnum





def readfile():
    with open('currency.txt') as currency:
        cur = currency.read()
        cur_split = cur.split()
        
    return cur_split



class UI:
    
    def __init__(self):
        exact = True
        myDict = {}
        try:
            for key, val in csv.reader(open('ccinfo.csv')):
                myDict[key] = val
        except:
            with open('ccinfo.csv','a'): pass
            
        finally:

            while exact:
                            
                line = input('>>> ').upper()
                x = line.split()

                    
                if x[0] == 'ISSUE':
                    if x[1] not in readfile():
                        print('NO_SUCH_CURRENCY')
                    elif Decimal(x[2]) < 0:
                        print('NEGATIVE_LIMIT')
                    else:
                        data = Credit_card(x[1], Money(x[1],0), Money(x[1],x[2]))
                        gennum = data.GenerateCard()
                        myDict[gennum] = data
                        print(myDict)
                        print('{} {}'.format('ISSUED', gennum))
                            
                            
                elif x[0] == 'PURCHASE':
                    if Decimal(x[3]) < 0:
                        print('NONPOSITIVE_AMOUNT')
                    elif x[2] not in readfile():
                        print('NO_SUCH_CURRENCY')
                    elif int(x[1]) not in myDict:
                        print('NO_SUCH_CARD')
                    else:
                        myDict[int(x[1])].purchase(Money(x[2],x[3]))
                        print(type(x[2]))
                        print(myDict)
                        print('AUTHORIZED {} {}'.format(myDict[int(x[1])].getcurrencycode(), myDict[int(x[1])].getbalance()))




                            
                        
                elif x[0] == 'PAYMENT':
                    if int(x[1]) not in myDict:
                        print('NO_SUCH_CARD')
                    elif x[2] not in readfile():
                        print('NO_SUCH_CURRENCY')
                    else:
                        myDict[int(x[1])].payment(Money(x[2],x[3]))
                        print('PAID {} {}'.format(myDict[int(x[1])].getcurrencycode(), myDict[int(x[1])].getbalance()))


                    
                elif x[0] == 'CANCEL':

                    if int(x[1]) in myDict:
                        del myDict[int(x[1])]
                        print('{} {}'.format('CANCELED', int(x[1])))
                    elif myDict[int(x[1])].getbalance().getmoney() != 0:
                        print('NONZERO_BALANCE')
                    elif int(x[1]) not in myDict:
                        print('NO_SUCH_CARD')

                                                            
                elif x[0] == 'EXIT':
                    w = csv.writer(open('ccinfo.csv','w'))
                    for key, val in myDict.items():
                        w.writerow([key,val])
                    exact = False
                    print('GOODBYE')
                
if __name__ == '__main__':
    UI()               

