# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:02:00 2020

@author: L
"""
import os
import re
from collections import Counter
c = Counter()  

mydir = r'C:\PATH'
findword = 'word'

def word_search(fpath, findword):
#    search0 = rf'\b{findword}\b'          #r'\bbob\b'      # matches bob
    search1 = rf'(?i)\b{findword}\b'      #r'(?i)\bbob\b'  # matches bob, Bob
#    search2 = rf'{findword}'              #r'bob'          # matches bob, Bob, bobcat  
  
    with open(fpath, encoding="utf-8", errors='ignore') as openfile:
        contents = openfile.read()
        count = sum(1 for match in re.finditer(search1, contents))
    openfile.close()
    return count

for f in os.listdir(mydir):
    if f.endswith(".txt"):
        fpath = os.path.join(mydir, f)
        print(f)
        print(word_search(fpath, findword))
  
