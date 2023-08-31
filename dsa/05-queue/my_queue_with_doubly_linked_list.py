from random import randint

class Node:

    # Function to initialise the node object
    def __init__(self, value):
        self.value = value # Assign value
        self.next = None # Initialize next as null
        self.prev = None # Initialize prev as null
		
class Queue:
    
    # Function to initialize the node
    def __init__(self):
        self.front = None
        self.rear = None
        
    # Function to add an element value in the Queue
    def enqueue(self, value):
        push_node = Node(value)
        
        if not self.rear:
            self.front = self.rear = push_node
            self.front.next = self.rear
            self.rear.prev = self.front
        else: # prevent created double rear node
            push_node.prev = self.rear # set the previous node as the previous object of the push_node
            self.rear.next = push_node # set the push_node node as the next object node of the previous node
            self.rear = push_node # set push_node as the current rear node 
        
        return self.rear.value
    
    # Function to check if the queue is empty or not
    def is_empty(self):
        if not self.front:
            return True
        return False
			
    # Function to remove first element and return the element from the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        
        pop_node = self.front.value
        self.front = self.front.next
        
        return pop_node

    # Function to return the size of the queue
    def queue_size(self):
        if self.is_empty():
            return "Queue is empty."
        
        curr = self.front
        len = 0
        
        while curr:
            len = len + 1
            curr = curr.next
        return len

    # Function to print the stack
    def print_queue(self):  
        if self.is_empty():
            return "Queue is empty."
        
        temp = self.front
        out = ""
        
        while temp:
            out += str(temp.value) + " "
            temp = temp.next
        
        return out
    
    # Prints rear element of the stack
    def rear_element(self):
        if self.is_empty():
            return "Queue is empty."
        else:
            return self.rear.value

    # Prints front element of the stack
    def front_element(self):
        if self.is_empty():
            return "Queue is empty."
        else:
            return self.front.value

def queue_info(queue):
    print(f"--------------- INFO ---------------")
    print(f"Stack Empty         : {queue.is_empty()}")
    print(f"Stack Content       : {queue.print_queue()}")
    print(f"Stack Count         : {queue.queue_size()}")
    print(f"Stack Front Element : {queue.front_element()}")
    print(f"Stack Rear Element  : {queue.rear_element()}\n")           
            	
if __name__=='__main__':
    # Start with the empty queue
    queue = Queue()
    
    for _ in range(10):
        push = queue.enqueue(randint(1, 9))
        print(f"Push: {push}")
    print()

    queue_info(queue)
    
    for _ in range(10):
        pop = queue.dequeue()
        print(f"Pop: {pop}")
    print()
    
    queue_info(queue)