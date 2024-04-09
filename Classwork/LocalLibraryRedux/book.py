class Book:
    def __init__(self):
        self.__id = 0
        self.__bookName = ""
        self.__bookAuthor = ""
        self.__bookGenre = ""
        self.__pageNum = 0
        self.__copiesNum = 0
    def getBookName(self):
        return self.__bookName
    def getBookAuthor(self):
        return self.__bookAuthor
    def getBookGenre(self):
        return self.__bookGenre
    def getPageNum(self):
        return self.__pageNum
    def getCopiesNum(self):
        return self.__copiesNum
    def setBookID(self,newID):
        self.__id = newID
    def setBookName(self, newName):
        self.__bookName = newName
    def setBookAuthor(self, newAuthor):
        self.__bookAuthor = newAuthor
    def setBookGenre(self, newGenre):
        self.__bookGenre = newGenre
    def setPageNum(self,newPageNum):
        self.__pageNum = newPageNum
    def setCopiesNum(self,newCopiesNum):
        self.__copiesNum = newCopiesNum