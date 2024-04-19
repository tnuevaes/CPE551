# Author: Teddy Nueva Espana
# Date: 4/19/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program sets up Nodes and Stack Classes 

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    def getData(self):
        return self.__data

    def setData(self,data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self,next):
        self.__next = next


class EmptyStackException(Exception):
    def __init__(self, exception):
        self.__message = f"Stack is empty, {exception} cannot be completed"
        super().__init__(self.__message)

class Stack:
    def __init__(self):
        self.__head = None
    
    def push(self, data):
        newNode = Node(data) 
        newNode.setNext(self.__head) #sets head node to the next node after new node, new node on top
        self.__head = newNode

    def pop(self):
        if self.__head == None:
            raise EmptyStackException("Pop()")
        else:
            data = self.__head.getData()
            self.__head = self.__head.getNext() #set head to next node, removes the current head
        return data
    
    def peek(self):
        if self.__head == None:
            raise EmptyStackException("peek()")
        else:
            data = self.__head.getData()
            return data

    def clear(self):
        self.__head = None # garbage collect after head is empty
      
    def __str__(self):
        if self.__head == None:
            return "Empty"
        
        output = ""
        current = self.__head
        while current.getNext() != None:  #iterate through connected nodes
            output += f"{current.getData()}, " #create single string with all node info
            current = current.getNext()
        
        output += f"{current.getData()}"
        
        return output
    
    
          
    
    
            
