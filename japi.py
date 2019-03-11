import json
import urllib.request
import os

def getStockData(s):
   
    #s="AAPL"
    k="8JOWD04BE01QXU5T"
    f="BATCH_STOCK_QUOTES"
    baseurl = "https://www.alphavantage.co/query?function="
    fullurl = baseurl + f + "&symbols=" + s + "&apikey=" + k

    connection = urllib.request.urlopen(fullurl)
    responseString = connection.read().decode()
    d_response = json.loads(responseString)
    price = d_response ['Stock Quotes'][0]['2. price']
    output = ('The current price of {} is: {}'.format(s, price))
    return output
def save_stockprice(path, filename, output):
    fpath = os.path.join(path, filename)
    if os.path.exists(fpath):
        with open  (fpath, 'a') as japi:
            japi.write(output)
            japi.write('\n')
            japi.close()
    else:
        with open  (fpath, 'w') as japi:
            japi.write(output)
            japi.write('\n')
            japi.close()
 
def main():
    while (True):
         s = input("Please enter your stock symbol or enter quit to end..")
         if s != 'quit':
            ps = getStockData(s)
            print('Stock Quotes retrieved successfully!')
            save_stockprice(r'C:\Users\16195\Desktop\now', 'japi.out', ps)
         else: break
        
main()