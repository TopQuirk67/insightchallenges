#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 08:05:03 2018

@author: topquirk67
"""
from bs4 import BeautifulSoup
import requests
import time
import random
from requests import session

username = 'ghouk@seattleacademy.org'
password = 'Got5Minuted'

payload = {'action'    : '/sessions',
           'email'     : username,  # this is from the 'name' tag
           'password'  : password}  # this is from the 'name' tag



session_requests = requests.session()
#login_url = "https://bitbucket.org/account/signin/?next=/"
#login_url = 'https://accounts.naviance.com/login?state=g6Fo2SBJS2Ewam95NFpOX1RaYU5kQ2tFVkJ0ZG45MG11MDZLSqN0aWTZMmdhRm8yU0J6YVcxU1dHUkJMVXhzTkdGUlpqUnpNV0poU1hka2MwZDBTMlZHVWtONmFRo2NpZNkgeXNFenE2a0lDaHlPcGdpMzc5RTFabzBVcmFQU2hWOWs&client=ysEzq6kIChyOpgi379E1Zo0UraPShV9k&protocol=oauth2&domain=accounts.naviance.com&connection=Username-Password-Authentication&audience=https%3A%2F%2Fid.naviance.com&scope=openid%20offline_access%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fid.naviance.com%2Foauth%2Fcallback&id_root_uri=https%3A%2F%2Fid.naviance.com&succeed_root_uri=https%3A%2F%2Fsucceed.naviance.com'
login_url = 'https://accounts.naviance.com/login'
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
## authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

#result = session_requests.post(
#	login_url, 
#	data = payload, 
#	headers = dict(referer=login_url)
#)



time.sleep(5)

url = 'https://succeed.naviance.com/studentsmain/index.php?letter=A'
#page = urllib2.urlopen(url)
# parse the html using beautiful soup and store in variable `soup`
#soup = BeautifulSoup(page, ‘html.parser’)
