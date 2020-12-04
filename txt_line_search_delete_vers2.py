# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:23:28 2020
txt_line_search_delete
delete specific lines according to words or all lines starting from a word
@author: L
"""

import os
import time


start_time = time.time()

delword = ['DELETE THIS WORD']
lastword = ['DELETE ALL WORDS FROM HERE']

path =      r'C:\PATHOLD'
pathnew = r'C:\PATHNEW'

dir = []

for f in os.listdir(path):
    if f.endswith(".txt"):
        if f not in dir:
            dir.append(f)
         
for f in dir:
    
    fpath = os.path.join(path, f)
    printline = True
    delrest = False
    fnew = f[:20]+ 'clean_' + f[20:]
    fpathnew = os.path.join(pathnew, fnew)

    with open(fpath, encoding="utf-8", errors='ignore') as input:
        with open(fpathnew, "w", errors='ignore') as output: 
           
            #delete first two lines
            next(input)
            output.write('\n')
            next(input)
            output.write('\n')

            for line in input:
                printline = True
                for word in delword:
                    if word in line:            
                        printline = False
                if printline == False:
                    output.write('\n')
                if printline == True:
                    output.write(line)

                        
    input.close()
    output.close()

print ("%.2f" % (time.time() - start_time), "seconds")


