#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:36:37 2019

@author: topquirk67
"""
from bs4 import BeautifulSoup
import requests

url = 'http://oldtownscrabble.com/05/12/bingo-stems-study-grids/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
x=soup.find_all('td',class_='column-2')
y = []
for item in x:
    y.append(item.contents[0])
