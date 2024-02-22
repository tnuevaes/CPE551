# Author: Teddy Nueva Espana
# Date: 2/16/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program prompts the user for a choice of art to 
# display as well as a symbol to be used as a border around the art

def intro():
    """Prompts user for input of art choice and border symbol, 
    returns art and border 
    """
    print("Welcome to painter!")
    print("Art choices: \n"
          "   1. Sleeping Cat \n"
          "   2. Sailing Ship \n"
          "   3. Slimy Snail\n"
          "   4. Dandy Dog\n")
    art = input("Enter number of which art to display:")
    border = input("Enter symbol to use as border:")
    return art, border
    
def printHeaderFooter(border, size):
    """Takes in two parameters, border and size prints a 
    line of the border character with length dependent on the size
    """
    HeadFoot = border * size
    print(HeadFoot)
   
def sleepingCat(border):
    """Takes in border (single character) parameter, prints lines of 
    the image of a sleeping cat surrounded by the border character.
    """
    cat1 = "      |\\      _,,,---,,_      "     
    cat2 = "ZZZzz /,`.-'`'    -.  ;-;;,_  "
    cat3 = "     |,4-  ) )-,_. ,\\ (  `'-' "
    cat4 = "    '---''(_/--'  `-'\\_)      "
    printHeaderFooter(border,len(cat1)+2)
    print(f"{border}{cat1}{border}")
    print(f"{border}{cat2}{border}")
    print(f"{border}{cat3}{border}")
    print(f"{border}{cat4}{border}")
    printHeaderFooter(border,len(cat1)+2)
    
def sailingShip(border):
    """Takes in border (single character) parameter, prints lines of 
    the image of a sailing ship surrounded by the border character.
    """
    ship1 = "      |    |    |            "
    ship2 = "     )_)  )_)  )_)           "
    ship3 = "    )___))___))___)\\         "
    ship4 = "   )____)____)_____)\\\\       "
    ship5 = " _____|____|____|____\\\\\\__   "
    ship6 = " \\    Satisfaction   /       "
    ship7 = "^^^^^^^^^^^^^^^^^^^^^^^^^^^^ "
    printHeaderFooter(border,len(ship1)+2)
    print(f"{border}{ship1}{border}")
    print(f"{border}{ship2}{border}")
    print(f"{border}{ship3}{border}")
    print(f"{border}{ship4}{border}")
    print(f"{border}{ship5}{border}")
    print(f"{border}{ship6}{border}")
    print(f"{border}{ship7}{border}")
    printHeaderFooter(border,len(ship1)+2)

def snail(border):
    """Takes in border (single character) parameter, prints lines of 
    the image of a snail surrounded by the border character.
    """
    snail1 ="         __,._        "
    snail2 ="        /  _  \\       "
    snail3 ="       |  6 \\  \\  oo  "
    snail4 ="        \\___/ .|__||  "
    snail5 =" __,..='"'^  . , '"'  , \\ "
    snail6 ="<.__________________/ "
    printHeaderFooter(border,len(snail1)+2)
    print(f"{border}{snail1}{border}")
    print(f"{border}{snail2}{border}")
    print(f"{border}{snail3}{border}")
    print(f"{border}{snail4}{border}")
    print(f"{border}{snail5}{border}")
    print(f"{border}{snail6}{border}")
    printHeaderFooter(border,len(snail1)+2)

def dog(border):
    """Takes in border (single character) parameter, prints lines of 
    the image of a dog surrounded by the border character
    """
    dog1 = "   / \\__       "
    dog2 = "  (    @\\___   "
    dog3 = "  /         O  "
    dog4 = " /   (_____/   "
    dog5 = "/_____/   U    "
    printHeaderFooter(border, len(dog1)+2)
    print(f"{border}{dog1}{border}")
    print(f"{border}{dog2}{border}")
    print(f"{border}{dog3}{border}")
    print(f"{border}{dog4}{border}")
    print(f"{border}{dog5}{border}")
    printHeaderFooter(border, len(dog1)+2)
    
def blank(border):
    """Takes in border (single character) parameter, prints 5x5 grid of empty space
    surrounded by border character 
    """
    line = "     "
    printHeaderFooter(border, len(line)+2)
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    printHeaderFooter(border, len(line)+2)