# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:53:08 2018
@author: lenovo
"""
import copy
from Node import function
import numpy as np

with open("activision.txt") as f1, open("vivendi.txt") as f2, \
        open("result.txt", "w") as f3:
    f3.write(f1.read().strip() + f2.read().strip())
mylist = np.loadtxt("result.txt")

TL = function()

Readvivendi = open('vivendi.txt') 
Linevivendi = Readvivendi.readline()

while Linevivendi:
    TL.append(int(Linevivendi)) 
    Linevivendi = Readvivendi.readline()
Readvivendi.close()


Readactivision = open('activision.txt')
Lineactivision = Readactivision.readline()

while Lineactivision:
    TL.append(int(Lineactivision))
    Lineactivision = Readactivision.readline()
Readactivision.close()

def find(LList):
    tempList = copy.copy(LList) 
    temp = LList.head
    duplicates = function()
    while temp != None:                     
        if tempList.search1(temp.getID()): 
            duplicates.append(temp.getID()) 
        temp1 = temp.getID() 
        temp = temp.getNext() 
        
    return duplicates  
    
dupes = find(TL)

print('There are {} duplicate IDs.'.format(dupes.size()))

def bubbleSort(arr): 
	n = len(arr) 

	# Traverse through all array elements 
	for i in range(n): 

		# Last i elements are already in place 
		for j in range(0, n-i-1): 

			# traverse the array from 0 to n-i-1 
			# Swap if the element found is greater 
			# than the next element 
			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

bubbleSort(mylist) 

print ("Sorted array is:") 
for i in range(len(mylist)): 
	print ("%d" %mylist[i]), 


def merge(t):
    t = list(t)
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            print ("Have duplicates"); 
            return 
    print ("Don't have duplicates"); 

print(merge(TL))

def boolean(LList):
    seen = [False for i in range(9999)] 
    current = LList.head
    duplicates = function()
    
    while current.getNext() is not None: 
        item = current.getID()           
        if seen[item]:
            duplicates.append(item)     
        else:
            seen[item] = True            
        current = current.getNext()  
    return duplicates

dupes = boolean(TL)
    
print('There are {} duplicate IDs.'.format(dupes.size()))


