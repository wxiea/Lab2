# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:53:08 2018
@author: lenovo
"""
import copy
from Node import function
import numpy as np
import sys
#save to one file #1
result=[]
with open('activision.txt','r') as f:
	for line in f:
		result.append(list(line.strip('\n').split(',')))

with open('vivendi.txt','r') as f:
	for line in f:
		result.append(list(line.strip('\n').split(',')))
#print(result)
#save to one file #2
"""
with open("activision.txt") as f1, open("vivendi.txt") as f2, \
        open("result.txt", "w") as f3:
    f3.write(f1.read().strip() + f2.read().strip())
mylist = np.loadtxt("result.txt")
"""
#save to one list #3
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
"""
def find(list):
    temp = list.head
    duplicates = function()
    while temp != None:    #compare                 
        if list.search(temp.getID()): 
            duplicates.append(temp.getID()) #add list to this list
        temp1 = temp.getID() #delete last ID
        list.removeNode(temp1)#to avoid it compare to it self
        temp = temp.getNext()#next
        
    return duplicates  
    
SOL = find(TL)

print('There are {} duplicate'.format(SOL.size()))
"""

def bubbleSort(alist):
    #cot = 0
    item = len(alist)-1
    while item > 0:
        for sort_item in range(0,item):
            #compare with the adjacent element
            #if alist[sort_item]==alist[sort_item+1]:
                #print("Have duplicates")
            if alist[sort_item]>=alist[sort_item+1]:
                #swap both elements
                alist[sort_item], alist[sort_item+1] = alist[sort_item+1], alist[sort_item]
        item-=1
 
bubbleSort(result)
#print(result)

"""
def merge(t):
    t = list(t)
    t.sort()#sort the list
    for i in range(len(t)-1):
        if t[i] == t[i+1]:#compare each one
            print ("Have duplicates"); 
            return 
    print ("Don't have duplicates"); 

print(merge(result))
"""
    
def merge_sort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2#Take the middle position
    #eft and right side
    left = li[:mid]
    right = li[mid:]
    #Split the left and right until there is only one element
    ll = merge_sort( left )
    rl =merge_sort( right )
    if ll == rl:
        print ("Have duplicate")     
    return merge(ll , rl)

def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0 :
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    #After loop, indicating that one of the arrays has no data
    #add another array to the result array.
    result += left
    result += right
    return result
li2 = merge_sort(result)
#print(li2)

def boolean(list):
    Blist = [False for i in range(1000)] #list of false
    current = list.head
    duplicates = function()   
    while current.getNext() is not None: #loop
        item = current.getID()#set item
        if Blist[item]:#if duplicates
            duplicates.append(item)#add
        else:
            Blist[item] = True#change statement    
        current = current.getNext()
    return duplicates

SOL = boolean(TL)
    
print('There are {} duplicate'.format(SOL.size()))
