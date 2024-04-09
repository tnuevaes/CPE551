class item: #Superclass
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__genre = ""
        self.__copies = 0

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getGenre(self):
        return self.__genre
    
    def getCopies(self):
        return self.__copies
    
    def setID(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setGenre(self, genre):
        self.__genre = genre

    def setcopies(self, copies):
        self.__copies = copies