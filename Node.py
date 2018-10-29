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

            
