#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:26:41 2018

@author: topquirk67
"""

import sys


if len(sys.argv)>2:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
elif len(sys.argv)>1:
    input_file = sys.argv[1]
    output_file = 'results.txt'
else:
    input_file = 'list.txt'
    output_file = 'results.txt'

print('input file :',input_file)
print('output file:',output_file)
