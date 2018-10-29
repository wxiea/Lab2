# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:53:08 2018
@author: lenovo
"""

class Node(object):
    item = -1
    next = None
    
    # Constructors #
    def __init__(self,item): 
        self.item = item
        self.next = None
        
            # Getters #
    def getID(self):
        return self.item

    def getNext(self):
        return self.next
    # Setters #
    def setID(self,newdata):
        self.item = newdata

    def setNext(self,newnext):
        self.next = newnext

        
class function:
    # Constructor #
    def __init__(self):
        self.head = None
    
        # Traverse list, counting elements to determine size #
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
            
        return count
    
        # Method to print linked list 
    def printList(self): 
        temp = self.head 
          
        while temp : 
            print(temp.data, end="->") 
            temp = temp.next
    
    # Function to add of node at the end. 
    def append(self, new_data): 
        new_node = Node(new_data) 
          
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
          
        while last.next: 
            last = last.next
        last.next = new_node 
        
    def search(self, item): #searches self for duplicates
        current = self.head
        current = current.getNext() # start search at node after our current one
        found = False               # otherwise we will always find the item
        while current != None and not found:    
            if current.getID() == item:
                  found = True
            else:
                  current = current.getNext()
        return found

    def removeNode(self,item):
        prev = None
        curr = self.head
        while curr:
            if curr.getID() == item:
                if prev:
                    prev.setNext(curr.getNext())
                else:
                    self.head = curr.getNext()
                return True
                    
            prev = curr
            curr = curr.getNext()
            
        return False
""" 
    def mergeSort(alist,node):

       if len(alist)>1:
           mid = len(alist)//2
           lefthalf = alist[:mid]
           righthalf = alist[mid:]   
           #recursion
           mergeSort(lefthalf)
           mergeSort(righthalf)
           i=0
           j=0
           k=0  
           while i < len(lefthalf) and j < len(righthalf):
               if lefthalf[i] < righthalf[j]:
                   alist[k]=lefthalf[i]
                   i=i+1
               else:
                   alist[k]=righthalf[j]
                   j=j+1
               k=k+1
           while i < len(lefthalf):
               alist[k]=lefthalf[i]
               i=i+1
               k=k+1
           while j < len(righthalf):
               alist[k]=righthalf[j]
               j=j+1
               k=k+1
"""



            
