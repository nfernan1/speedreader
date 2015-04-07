import urllib.request
import http.client
import urllib.error

# create a variable and concatenate strings

URL = 'http://ichart.yahoo.com/table.csv?s=GOOG&a=2&b=1&c=2011&d=10&e=30&f=2012&g=d'
webpage = urllib.request.urlopen(URL)
data = webpage.read()

##def show_url_contents():
##    while True:
##        url = 
##    
##def _print_url_contants(response http.client.HTTPResponse):
##    content_bytes = response.read()
##    content_string = content_bytes.decode(encoding = 'utf-8')
##    content_lines = content_string.splitlines()
##
##    
##
##def DL(URL:'a string'):
##    try:
##        webpage = urllb.request.urlopen(URL)
##        _print_url_contants(response)
##        
##
##    finally:
##        webpage.close()



def show_url_contents(url:str) -> None:
##    while True:
    if len(url) == 0:
        return
    else:
        _download_and_print_url(url)





def _download_and_print_url(url: str) -> None:

    response = None

    try:
        response = urllib.request.urlopen(url)
        _print_url_contents(response)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Ticker symbol does not exist')
        print('Status code: {}'.format(e.code))
        print()

    finally:
        if response != None:
            response.close()



def _print_url_contents(response: http.client.HTTPResponse) -> None:
    date = []
    price = []
    content_bytes = response.read()
    content_string = content_bytes.decode(encoding='utf-8')
    content_lines = content_string.splitlines()


    for line in content_lines:
        temp = line.split(',')
        date.append(temp[0])
        price.append(temp[4])
        dates = sorted(date[1:])
        prices = sorted(price[1:])
##        dates.extend(price)

    print('Date'+'\t\t'+'Close')
    for val,vals in zip(dates, prices):
        print(val+'\t'+vals)



    print()
    print()




if __name__ == '__main__':
    show_url_contents('http://ichart.yahoo.com/table.csv?s=GOOG&a=2&b=1&c=2011&d=2&e=10&f=2011&g=d')
    
