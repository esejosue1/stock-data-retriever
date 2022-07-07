#get stock history
import requests
from datetime import datetime
import time

#get input stock name, datetime from to
stock=input("Enter a stock: ")
sotck=stock.upper()
from_date=input('Enter a star date in yyyy/mm/dd format: ')
to_date=input('Enter an end date in yyyy/mm/dd format: ')

#convert our user input into string time
from_datetime=datetime.strptime(from_date, '%Y/%m/%d')
to_datetime=datetime.strptime(to_date, '%Y/%m/%d')

#convert our date string into an int, craeting tuples
from_epoch=int(time.mktime(from_datetime.timetuple()))
to_epoch=int(time.mktime(to_datetime.timetuple()))

#query found in yahoo stocks to download the history of a stock, 'downloads buttton'
url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

#header to get access to the info
headers= {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

#get the content of the url
content=requests.get(url, headers=headers).content
print(content)
#open a new file with the stock history
with open('data.csv', 'wb') as file:
  file.write(content)