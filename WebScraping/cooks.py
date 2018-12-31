#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 15:40:05 2018

@author: topquirk67
"""

from bs4 import BeautifulSoup
import requests
import time
import random
from requests import session

username = 'gareth.houk@gmail.com'
password = 'GooboMakarena11'

payload = {'action': '/sessions',
           'user[email]'     : username,
           'user[password]'  : password}

# the next 3 lines are pretty much copied from a different StackOverflow
# question. I don't really understand what they're doing, and obviously these 
# are where the problem is.

login_url = 'https://www.cooksillustrated.com/sign_in?return_to=https%3A%2F%2Fwww.cooksillustrated.com%2Fuser'
# =============================================================================
# source = requests.get(login_url).text
# soup = BeautifulSoup(source, "lxml")
# blub = soup.find('div',class_='auth__content')
# blub.find('form')
# blub.form.find_all('label')
# 
# =============================================================================
with session() as c:
    c.post(login_url, data=payload)
    response = c.get('https://www.cooksillustrated.com/recipes/browse')
    
soup = BeautifulSoup(response.content, "lxml")
recipe_grid=soup.find('div',class_='browse-results grid recipes')
this_page_recipes = recipe_grid.find_all('div',class_='result recipe title-long')
for this_recipe in this_page_recipes:
    image_file_wrap = this_recipe.find('div',class_='result__image-wrapper').a
    recipe_name = this_recipe.a['href'].split('/')[2]
    image_url = image_file_wrap.img['data-src']
    response = requests.get(image_url).content
    with open('cooks_images/' + recipe_name + '.jpeg', 'wb') as f:
        f.write(response)
    timeDelay = random.uniform(1.1, 3.5)
    time.sleep(timeDelay)

