dirt_x = 0
dirt_y = 9

dock_x = 0 
dock_y = 0

roomba_x = dock_x
roomba_y = dock_y

clean = 0

def cleanfun(roomba_x,roomba_y):
    while clean == 1:
        if roomba_y != 0:
            roomba_y -= 1
        if roomba_x != 0:
            roomba_x -= 1
        elif roomba_x == 0 and roomba_y == 0 :
            print(f"Roomba is back at {roomba_x}, {roomba_y}") 
            break
    

while clean == 0:
        if roomba_x == 0 : #hitting a wall on the left
            for j in range(0,9): #go right 
                roomba_x += 1 #increment x
                print(f"Roomba moves to {roomba_x},{roomba_y}")
                if (roomba_x == dirt_x and roomba_y == dirt_y): # found dirt
                    print(f"Roomba found dirt at {roomba_x},{roomba_y}")
                    clean = 1
                    cleanfun(roomba_x,roomba_y) #return
                    break
        if roomba_x == 9 and roomba_y < 9: # hitting a wall on the right
            roomba_y += 1 #increment y 
            print(f"Roomba moves to {roomba_x},{roomba_y}") 
            for k in range(0,9) : #decrement x till you hit a wall
                roomba_x -= 1
                if roomba_x == 0 and roomba_y < 9 : 
                    roomba_y += 1 
                print(f"Roomba moves to {roomba_x},{roomba_y}")
                if (roomba_x == dirt_x and roomba_y == dirt_y): # found dirt
                    print(f"Roomba found dirt at {roomba_x},{roomba_y}")
                    clean = 1
                    cleanfun(roomba_x,roomba_y) #return
                    break


            
            
            
    
