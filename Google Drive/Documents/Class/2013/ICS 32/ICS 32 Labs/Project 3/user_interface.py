import datetime
import dlfile

##http://ichart.yahoo.com/table.csv?s=SYMBOL
##&a=START_MONTH&b=START_DAY&c=START_YEAR
##&d=END_MONTH&e=END_DAY&f=END_YEAR&g=d

def _length(num:int):
    return len(str(num))


def start_date():
    '''Prints start date in format YYYY-MM-DD'''
    now = datetime.datetime.now()
    
    while True:
        start = input("Enter a start date in the format: YYYY-MM-DD: ").replace('-',' ')
        sdate = [int(num) for num in start.split()]

        current_date = now.strftime("%Y-%m-%d")
        if start > current_date:
            print('Invalid. Date inputted hasn\'t happened yet.')
        elif _length(sdate[0]) != 4 or _length(sdate[1]) != 2 and _length(sdate[2]) != 2:
            print('Invalid format.')
        else:
            print('{}-{}-{}'.format(sdate[0],sdate[1],sdate[2]))
            break



def end_date():
    '''Prints end date in foromat YYYY-MM-DD'''
    now = datetime.datetime.now()
    
    while True:
        end = input("Enter an end date in the format: YYYY-MM-DD: ").replace('-',' ')
        edate = [int(num) for num in end.split()]

        current_date = now.strftime("%Y-%m-%d")
        if end > current_date:
            print('Invalid. Date inputted hasn\'t happened yet.')
        elif _length(edate[0]) != 4 or _length(edate[1]) != 2 and _length(edate[2]) != 2:
            print('Invalid format.')
        else:
            print('{}-{}-{}'.format(edate[0],edate[1],edate[2]))
            print(edate[1])
            break


def user_interface():
    now = datetime.datetime.now()

    #Ticker symbol 
    symbol = input('Enter a ticker symbol: ').upper()


    #Start date in format YYYY-MM-DD
    while True:
        start = input("Enter a start date in the format: YYYY-MM-DD: ").replace('-',' ')
        sdate = [int(num) for num in start.split()]

        current_date = now.strftime("%Y-%m-%d")
        if start > current_date:
            print('Invalid. Date inputted hasn\'t happened yet.')
        elif _length(sdate[0]) != 4 or _length(sdate[1]) != 2 and _length(sdate[2]) != 2:
            print('Invalid format.')
        else:
            print('{}-{}-{}'.format(sdate[0],sdate[1],sdate[2]))
            break

        

    #End date in format YYYY-MM-DD   
    while True:
        end = input("Enter an end date in the format: YYYY-MM-DD: ").replace('-',' ')
        edate = [int(num) for num in end.split()]

        current_date = now.strftime("%Y-%m-%d")
        if end > current_date:
            print('Invalid. Date inputted hasn\'t happened yet.')
        elif _length(edate[0]) != 4 or _length(edate[1]) != 2 and _length(edate[2]) != 2:
            print('Invalid format.')
        else:
            print('{}-{}-{}'.format(edate[0],edate[1],edate[2]))
            break


    url = 'http://ichart.yahoo.com/table.csv?s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d'.format(symbol,(sdate[1]-1),sdate[2],sdate[0],(edate[1]-1),edate[2],edate[0])
    print(url)

    files = dlfile.show_url_contents(url)


user_interface()

