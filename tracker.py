__author__ = 'oddtazz'

import requests
import threading2

def gets(url, verifyval = True):
    try:
        r = requests.get(url, verify=verifyval)
        rjson = r.json()
        return rjson
    except ValueError:
        print "Something went wrong with " + url


def cryptsyprice():
    cryptsy = gets('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
    print "Cryptsy = %.8f" % float(cryptsy['return']['markets']['DOGE']['lasttradeprice'])
    print "Sell price = %.8f \t Buy price = %.8f" % (float(cryptsy['return']['markets']['DOGE']['sellorders'][0]['price']), float(cryptsy['return']['markets']['DOGE']['buyorders'][0]['price']))

def bterprice():
    bter = gets('http://data.bter.com/api/1/ticker/doge_btc')
    print "Bter = %.8f" % float(bter['last'])
    print "Sell price = %.8f \t Buy price = %.8f" % (float(bter['sell']), float(bter['buy']))

def bitterexprice():
    bittrex = gets('https://bittrex.com/api/v1.1/public/getticker?market=BTC-DOGE')
    print "Bittrex = %.8f" % float(bittrex['result']['Last'])
    print "Sell price = %.8f \t Buy price = %.8f" % (float(bittrex['result']['Ask']), float(bittrex['result']['Bid']))

def preludeprice():
    prelude = gets('https://api.prelude.io/last/DOGE', verifyval=False)
    print "Prelude = %.8f" % float(prelude['last'])

def mintpalprice():
    mintpal = gets('https://api.mintpal.com/market/stats/DOGE/BTC')
    print "Mintpal = %.8f" % float(mintpal[0]['last_price'])
    print "Sell price = %.8f \t Buy price = %.8f" % (float(mintpal[0]['top_ask']), float(mintpal[0]['top_bid']))

def pricetimer():
    threading2.Timer(2.0, pricetimer).start()
    cryptsyprice()
    bterprice()
    bitterexprice()
    preludeprice()
    mintpalprice()

pricetimer()