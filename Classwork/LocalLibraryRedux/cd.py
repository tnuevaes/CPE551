class CD:
    def __init__(self):
        self.__musicId = 0
        self.__albumName = ""
        self.__artistName = ""
        self.__genre = ""
        self.__numSongs = 0
        self.__numCopies = 0

    def getMusicId(self):
        return self.__musicId
    
    def setMusicId(self, musicId):
        self.__musicId = musicId

    def getAlbumName(self):
        return self.__albumName
    
    def setAlbumName(self, albumName):
        self.__albumName = albumName

    def getArtistName(self):
        return self.__artistName
    
    def setArtistName(self, artistName):
        self.__artistName = artistName

    def getGenre(self):
        return self.__genre
    
    def setGenre(self, genre):
        self.__genre = genre

    def getNumSongs(self):
        return self.__numSongs
    
    def setNumSongs(self, numSongs):
        self.__numSongs = numSongs

    def getNumCopies(self):
        return self.__numCopies
    
    def setNumCopies(self, numCopies):
        self.__numCopies = numCopies