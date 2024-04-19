# Author: Teddy Nueva Espana
# Date: 4/19/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program uses the Queue class to read through a list and produce a Queue 


from Queue import Queue

def main():
    
    queue = Queue()
    inputFile = open("inputQueue.txt","r")
    
    for line in inputFile:
        split = line.strip().split()
        action = split[0]
        if len(split) > 1:
            item = split[1]
        else: item = None
        
        if action == "enqueue":
            queue.enqueue(item)
            print(f"enqueued {item}")
        elif action == "dequeue":
            try:
                print(f"dequeued {queue.dequeue()}")    
            except Exception:
                print("Queue empty, cannot dequeue")
        elif action == "peek":
            try:
                print(f"peeked at {queue.peek()}")
            except:
                print("Queue empty, cannot peek")
        elif action == "clear":
            queue.clear()
            print("Clearing the queue")
        elif action == "print":
            print(queue)
    
main()
        
    