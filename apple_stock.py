#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An introduction to BeautifulSoup for Apple Stocks."""
#Author: Erica Liz

import urllib2
from bs4 import BeautifulSoup
import json

url = 'http://finance.yahoo.com/q/\
hp?s=AAPL&a=11&b=12&c=1980&d=10&e=2&f=2015&g=d'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
#print soup.prettify()


def apple_stock():
    """Some Apple stats from Yahoo Finance."""
    data = []
    fhandler = soup.find_all('tr')

    for rows in fhandler:
        try:
            if len(rows.find_all(('td', {'class': 'yfnc_tabledata1'}))) == 7:
                date = rows.contents[0].get_text()
                close = rows.contents[6].get_text()
                data.append((date, close))
                json_string = {
                'Date': date,
                'Close_Price': close,
                }
                print(json.dumps(json_string))
        except:
            print 'This is corrupt'
            continue
    return apple_stock
    

if __name__ == "__main__":
    apple_stock()
