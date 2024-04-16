class item: #Superclass
    def __init__(self, id, name, genre, copies):
        self._id = 0
        self._name = ""
        self._genre = ""
        self._copies = 0

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getGenre(self):
        return self._genre
    
    def getCopies(self):
        return self._copies
    
    def setID(self, id):
        self._id = id

    def setName(self, name):
        self._name = name

    def setGenre(self, genre):
        self._genre = genre

    def setCopies(self, copies):
        self._copies = copies