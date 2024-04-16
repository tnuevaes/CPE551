from item import item
class Book(item):
    def __init__(self, id, name, genre, copies):
        super().__init__(id, name, genre, copies)
        self.__bookAuthor = ""
        self.__pageNum = 0
 
    def getBookAuthor(self):
        return self.__bookAuthor
    def getPageNum(self):
        return self.__pageNum
    
    def setBookAuthor(self, newAuthor):
        self.__bookAuthor = newAuthor
    def setPageNum(self,newPageNum):
        self.__pageNum = newPageNum
