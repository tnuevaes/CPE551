# Author: Teddy Nueva Espana
# Date: 4/19/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program sets up Nodes and Queue Classes 

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


class EmptyQueueException(Exception):
    def __init__(self, exception):
        self.__message = f"Queue is empty, {exception} cannot be completed" 
        super().__init__(self.__message)
        
class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        
    def enqueue(self, data):
        newNode = Node(data) #Create new node instance
        if self.__head == None: #check if queue is empty
            self.__head = newNode #Set head and tail to new node instance
            self.__tail = newNode
        else:
            self.__tail.setNext(newNode) #if queue is not empty, new node is added to the end of queue
            self.__tail = newNode
    
    def dequeue(self):
        if self.__head == None:
            raise EmptyQueueException("dequeue()") #check if queue is empty
        else:
            data = self.__head.getData()
            self.__head = self.__head.getNext() #retreives data from head and sets head to the next node
            if self.__head == None: #one item
                self.__tail = None
            return data
    
    def peek(self):
        if self.__head == None:
            raise EmptyQueueException("dequeue()")
        else:
            data = self.__head.getData()
            return data
    
    def clear(self): 
        self.__head = None #removes all node info from head and tail
        self.__tail = None
        
    def __str__(self):
        if self.__head == None:
            return "Empty"
        
        output = ""
        current = self.__head
        while current.getNext() != None: #iterate through connected nodes
            output += f"{current.getData()}, " #create single string with all node info
            current = current.getNext()
        
        output += f"{current.getData()}" #create single string with all node info
        
        return output