import re

# Use day_dict and is_leap_year in your tomorrow function

day_dict ={ 1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
           10 : 31, 
           11 : 30,
           12 : 31} 

def is_leap_year(year:int)->bool:
    return (year%4 == 0 and year%100!= 0) or year%400==0

def days_in(month:int,year:int)->int:
    return (29 if month==2 and is_leap_year(year) else day_dict[month])


def tomorrow(date:str)->str:
    m = re.match(r'(1[0-2]|[1-9])/([0-2]?\d|3[01])/(\d{2}(?:\d\d)?)$',date)
    assert m, 'tomorrow: date format('+str(str)+') incorrect'
    month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    year += (0 if len(m.group(3))==4 else 2000)
    assert 1<=day<=days_in(month,year), 'tomorrow: day('+str(day)+') in date('+str(date)+') incorrect'
    day += 1
    if day > days_in(month,year):
        day,month = 1,month+1
    if month > 12:
        month,year = 1, year+1
    return str(month)+'/'+str(day)+'/'+str(year)


def expand(pat_dict:{str:str}):
    recognize = re.compile(r'#[^#]+#')
    expanded = True
    while expanded:
        expanded = False
        for p in pat_dict:
            m = recognize.search(pat_dict[p])
            if m:
                expanded = True
                pat_dict[p] = recognize.sub('('+pat_dict[m.group(0)[1:-1]]+')',pat_dict[p],1)





if __name__ == '__main__':
    import driver, prompt
    if prompt.for_bool('Test tomorrow?',True):
        driver.driver() # type quit in driver to return and execute  code below
    
    if prompt.for_bool('Test expand?',True):
        pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
        expand('result =',pd)
        print(pd)
        # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
        
        pd = dict(integer       =r'[+-]?\d+',
                  integer_range =r'#integer#(..#integer#)?',
                  integer_list  =r'#integer_range#(?,#integer_range#)*',
                  integer_set   =r'{#integer_list#?}')
        expand(pd)
        print('result =',pd)
        # produces/prints the dictionary 
        # {'integer'      : '[+-]?\\d+',
        #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
        #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
        #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
        # }
