# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:53:08 2018

@author: lenovo
"""

import os
import os.path
import numpy as np
import itertools

#in to one file
with open("activision.txt") as f1, open("vivendi.txt") as f2, \
        open("result.txt", "w") as f3:
    f3.write(f1.read().strip() + f2.read().strip())
mylist = np.loadtxt("result.txt")

#sol 1
def find(ID):
    mylist = np.loadtxt("result.txt")
    for i in range(len(mylist)):
        if mylist[i] == ID:
            print ("Find" )
            return ID
    else:
        print("Didn't find")
find(399999)   
 
#sol 2   
def bubble(list):       
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
    return list
 
result = bubble(mylist)
for i in range(len(result)): 
   print (result[i]); 
   
#sol 3
def merge(t):
    t = list(t)
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            print ("Have duplicates"); 
            return 
    print ("Don't have duplicates"); 

print(merge(result))


