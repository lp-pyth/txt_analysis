# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:24:38 2021

@author: Mr
"""

import os

path = r'C:\Users\Mr\Documents\GitHub\Workshop-ML-Automatisierte-Inhaltsanalyse\Kubilari_clean'
pathnew = r'C:\C:\Users\Mr\Documents\GitHub\Workshop-ML-Automatisierte-Inhaltsanalyse'


dir = []
dirtxt = []

for f in os.listdir(path):
    if f.endswith(".txt"):
        if f not in dir:
            dir.append(f)
         
for f in dir:
    
    fpath = os.path.join(path, f)
    print(f)
    with open(fpath) as f:
        lines = f.readlines()
    line = '\t'.join([line.strip() for line in lines])
    print(line)