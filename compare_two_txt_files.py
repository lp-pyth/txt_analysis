# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:22:00 2020
Compare two text files in terms of word overlap
@author: L
"""

import time


start = time.time()

file1 = r'C:\\FILE1.txt'
file2 = r'C:\\FILE2.txt'


words1 = set(open(file1).read().split())
words2 = set(open(file2).read().split())
          
#print('Word Count 1: ', len(words1))
#print('Word Count 2: ', len(words2))

duplicates = words1.intersection(words2)
uniques = words1.difference(words2).union(words2.difference(words1))
overlap = len(duplicates)/(len(duplicates)+len(uniques))
print ("Overlap: ", "%.2f" % overlap)



#if (overlap>0.9):
#    print ('File: ', file1)
#    print ('File: ', file2)
#    print ("Overlap: ", "%.2f" % overlap)
    #print ("Duplicates(%d):%s"%(len(duplicates),duplicates))
    #print ("\nUniques(%d):%s"%(len(uniques),uniques))
    

end = time.time()
print('Hours', (end-start)*100812900/3600)  
    
    
    
    
    
