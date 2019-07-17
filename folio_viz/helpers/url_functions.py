import requests
import json

def get_fundamentals(symbol, api_key):
    url = 'https://eodhistoricaldata.com/api/fundamentals/{}?fmt=json&api_token={}'.format(symbol, api_key)
    return requests.get(url).json()

def get_realTime(symbol, api_key):
    url = 'https://eodhistoricaldata.com/api/real-time/{}?fmt=json&api_token={}'.format(symbol, api_key)
    return requests.get(url).json()

def get_eodQuote(symbols, api_key):
    url = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/US?api_token={}&fmt=json&symbols='.format(api_key)
    for symbol in symbols:
        url += str(symbol) + ','
    url = url[:-1]
    return requests.get(url).json()

def get_bulkRealTime(symbols, api_key):
    url = 'https://eodhistoricaldata.com/api/real-time/{}?api_token={}&fmt=json&s='.format(str(symbols[0]), api_key)
    print(url)
    for symbol in symbols[1:]:
        url += str(symbol) + ','
    url = url[:-1]
    return requests.get(url).json()

    