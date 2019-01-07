#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:36:25 2018

@author: topquirk67, Gary Houk. 
"""

## Final code (well, almost final, it needs to put into an inline .py file)
# Program specs:
# Take a list of strings, filter out non-numerical and non-letter (UC or LC) characters
# Order ascending the numerical and letter strings
# Return list of strings with the input list's structure in terms of string/letter etc.
#
# Imports
import sys
import re

if len(sys.argv)>2:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
elif len(sys.argv)>1:
    input_file = sys.argv[1]
    output_file = 'results.txt'
else:
    input_file = 'list.txt'
    output_file = 'results.txt'

#### function definitions
def str_type(s):
    if s[0] in '0123456789':
        return 'n' # number-like
    else:
        return 'w' # word-like

def scrub_order(input_string):
    # Takes a string as input
    input_list = input_string.split()
    # Here we are using regular expression matching from the re package
    # Note that spaces are replaced and that case remains the same
    scrubbed_list = [re.sub(r'[^0-9a-zA-Z]', "",item) for item in input_list]    

    # make a list of the type of item, either 'n' or 'w' for number- or word-like
    w  = sorted([item for item in scrubbed_list if item[0] not in '0123456789'],key=str.lower)
    n  = sorted([item for item in scrubbed_list if item[0]     in '0123456789'],key=str.lower)
    output_list = []
    for item in scrubbed_list:
        if (item[0] in '0123456789'):
            output_list.append(n.pop(0))
        else:
            output_list.append(w.pop(0))
    return ' '.join(output_list) # return a string rather than a list

#### now open the file and call functions
with open(input_file, 'r') as f:
    data = f.readlines()  # allow multiple lines; just treat each one separately
f.close()

output_lines = []
for line in data:
    output_lines.append(scrub_order(line))

f_out = open(output_file,'w')
for line in output_lines:
    f_out.write(line+'\n')
f_out.close()
