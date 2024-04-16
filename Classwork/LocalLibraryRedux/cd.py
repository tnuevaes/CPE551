from item import item
class cd(item):
    def __init__(self, id, name, genre, copies):
        super().__init__(id, name, genre, copies)
        self.__artistName = ""
        self.__numSongs = 0

       
    def getArtistName(self):
        return self.__artistName
    
    def setArtistName(self, artistName):
        self.__artistName = artistName

    def getNumSongs(self):
        return self.__numSongs
    
    def setNumSongs(self, numSongs):
        self.__numSongs = numSongs