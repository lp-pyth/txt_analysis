# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:02:00 2020

@author: L
"""
import os
from collections import Counter


mydir = r'C:\folder'
findword = 'findword'
wordlength = 6

def common_words(fpath):
    with open(fpath, encoding="utf-8", errors='ignore') as openfile:
        #count = Counter(word for line in openfile for word in line.split())  
        count = Counter(word for line in openfile for word in line.split() 
                        if len(word) >= wordlength)  
    openfile.close()
    return count.most_common(10)

def count_capital_words(fpath):                                               
    count = 0                                                                    
    with open(fpath, encoding="utf-8", errors='ignore') as openfile:                                             
        for line in openfile:
            for word in line.split():  
                if len(word) >= wordlength:
                    if word.istitle(): 
                        count=Counter(word) 
    openfile.close()                                               
    return count.most_common(10)

for f in os.listdir(mydir):
    if f.endswith(".txt"):
        fpath = os.path.join(mydir, f)
        print(f)
       # print(common_words(fpath))
        print(count_capital_words(fpath))
  

