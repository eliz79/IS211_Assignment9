#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An introduction to BeautifulSoup for NFL Stats."""
#Author: Erica Liz

import urllib2
from bs4 import BeautifulSoup
import json

url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/\
year-2015-season-regular-category-touchdowns' 
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
#print soup.prettify()


def NFLStats():
    """Some footballs stats from CBS for touchdowns."""
    td_list = []
    fhandler = soup.find_all(class_= {'row1', 'row2'})

    for tds in fhandler[:20]:
        try:
            player = tds.contents[0].get_text()
            position = tds.contents[1].get_text()
            touch_downs = tds.contents[6].get_text()
            team = tds.contents[2].get_text()
            json_string = {
            "Name": player,
            "Position": position,
            "Touchdowns" : touch_downs, 
            'Team' : team
            }
            print(json.dumps(json_string))
            
        except:
            print 'This is corrupt'
            continue
    
    return td_list


if __name__ == "__main__":
    NFLStats()
