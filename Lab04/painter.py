# Author: Teddy Nueva Espana
# Date: 2/16/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program prompts the user for a choice of art to 
# display as well as a symbol to be used as a border around the art

def intro():
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
    HeadFoot = border * size
    print(HeadFoot)
   
def sleepingCat(border):
    cat1 = "      |\\\\      _,,,---,,_      "     
    cat2 = "ZZZzz /,`.-'`'    -.  ;-;;,_   "
    cat3 = "     |,4-  ) )-,_. ,\\\\ (  `'-' "
    cat4 = "    '---''(_/--'  `-'\\\\_)      "
    printHeaderFooter(border,len(cat1)+2)
    print(f"{border}{cat1}{border}")
    print(f"{border}{cat2}{border}")
    print(f"{border}{cat3}{border}")
    print(f"{border}{cat4}{border}")
    printHeaderFooter(border,len(cat1)+2)
    
def sailingShip(border):
    ship1 = "      |    |    |            "
    ship2 = "     )_)  )_)  )_)           "
    ship3 = "    )___))___))___)\\\\        "
    ship4 = "   )____)____)_____)\\\\\\\\     "
    ship5 = " _____|____|____|____\\\\\\\\\\\\__"
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
    line = "     "
    printHeaderFooter(border, len(line)+2)
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    print(f"{border}{line}{border}")
    printHeaderFooter(border, len(line)+2)

def main():
    art, border = intro()
    if art == "1":
        sleepingCat(border)
    elif art == "2":
        sailingShip(border)
    elif art == "3":
        snail(border)
    elif art == "14":
        dog(border)
    else:
        blank(border)
        print("We do not seem to have that painting")

        exit(-1)
    print("I hope you enjoy the art!")        
    
main()
