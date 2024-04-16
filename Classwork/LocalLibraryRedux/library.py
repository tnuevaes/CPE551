from book import Book
from movies import Movie
from cd import cd
import item

def main():
    books = []
    movies = []
    cds = []
    
    items = []
    
    Inventory = open("libraryInventory.txt", "r")
    
    for line in Inventory:
        line = line.strip()
        lineList = line.split(",") 
        #format: [0] = ID, [1] = Type, [2] = Title, 
        if lineList[1] == "Book":
            #Book code
            #format: [0] = ID, [1] = Type, [2] = Title, [3] = Author, [4] = Genre, [5] = Pages, [6] = copies 
            NewBook = Book(lineList[0], lineList[2], lineList[4], lineList[6])

            NewBook.setID(lineList[0])
            NewBook.setName(lineList[2])
            NewBook.setBookAuthor(lineList[3]) #Not superclass
            NewBook.setGenre(lineList[4])
            NewBook.setPageNum(lineList[5]) #Not superclass
            NewBook.setCopies(lineList[6])
            
            items.append(NewBook)
            
        if lineList[1] == "Movie":
            #Movie code
            NewMovie = Movie(lineList[0], lineList[2], lineList[3], lineList[5])

            NewMovie.setID(lineList[0])
            NewMovie.setName(lineList[2])
            NewMovie.setGenre(lineList[3])
            NewMovie.setLength(lineList[4]) #Not superclass
            NewMovie.setCopies(lineList[5])
            items.append(NewMovie)
            
        if lineList[1] == "Music":
            #Music code
            NewMusic = cd(lineList[0], lineList[2], lineList[4], lineList[6])
            
            NewMusic.setID(lineList[0])
            NewMusic.setName(lineList[2])
            NewMusic.setArtistName(lineList[3]) #Not superclass
            NewMusic.setGenre(lineList[4])
            NewMusic.setNumSongs(lineList[5]) #Not superclass
            NewMusic.setCopies(lineList[6])
            items.append(NewMusic)

    for item in items:
        name = item.getName()
        id = item.getID()
        genre = item.getGenre()
        copies = item.getCopies()
        
        print(f"""
name: {name}
id: {id}
genre: {genre}
# of copies: {copies}""")
        
        if isinstance(item, Book):
            author = item.getBookAuthor()
            pages = item.getPageNum()
            print("Book")
            print(f"Author: {author}")
            print(f"# of pages: {pages}")
                
        elif isinstance(item, cd):
            artist = item.getArtistName()
            songs = item.getNumSongs()
            print("CD")
            print(f"artist: {artist}")
            print(f"# of songs: {songs}")
        elif isinstance(item, Movie):
            length = item.getLength()
            print("Movie")
            print(f"Length in minutes: {length}")

    
            
            

            
main()