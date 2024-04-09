from item import item
class Movie(item):
    def __init__(self, id, name, genre, copies):
        super().__init__(id, name, genre, copies)
        self.__length = 0


    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length
