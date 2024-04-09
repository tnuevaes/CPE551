import book
import movies
import cd

def main():
    books = []
    movies = []
    cds = []
    
    Inventory = open("libraryInventory.txt", "r")
    
    for line in Inventory:
        line = line.strip()
        lineList = line.split(",") 
        #format: [0] = ID, [1] = Type, [2] = Title, 
        if lineList[1] == "Book":
            #Book code
            #format: [0] = ID, [1] = Type, [2] = Title, [3] = Author, [4] = Genre, [5] = Pages, [6] = copies 
            NewBook = book()
            NewBook.setID(lineList[0])
            NewBook.setBookName(lineList[2])
            NewBook.setBookAuthor(lineList[3])
            NewBook.setBookGenre(lineList[4])
            NewBook.setPageNum(lineList[5])
        if lineList[1] == "Movie":
            #Movie code
            NewMovie = movies()
            NewMovie.setID(lineList[0])
            NewMovie.setName(lineList[2])
            NewMovie.setGenre(lineList[3])
            NewMovie.setLength(lineList[4])
            NewMovie.setCopies(lineList[5])
            
        if lineList[1] == "Music":
            #Music code
            NewMusic = cd()
            NewMusic.setID(lineList[0])
            NewMusic.setName(lineList[2])
            NewMusic.setArtistName(lineList[3])
            NewMusic.setGenre(lineList[4])
            NewMusic.setNumSongs(lineList[5])
            NewMusic.setCopies(lineList[6])
            
