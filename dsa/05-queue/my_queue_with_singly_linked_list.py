from random import randint

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0 # only cache and separated with node
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    # String representation of the stack
    def __str__(self):
        cur = self.front
        out = ""
        
        while cur:
            out += str(cur.value) + " "
            cur = cur.next # change to next node
            
        if out:
            return out
        else:
            return "Queue is Empty."
    
    # Method to add an item to the queue
    def push(self, value):
        push_node = Node(value)
        self.size += 1 # only cache and separated with node
        
        if not self.front:
            self.front = self.rear = push_node # must be equal
        
        self.rear.next = push_node # set the push_node as the next object of previous rear node
        self.rear = push_node # set the push_node as the new rear object
        
        return self.rear.value

	# Method to remove an item from queue
    def pop(self):
        if self.is_empty():
            return
        
        pop_node = self.front # set the front node to pop as pop_node
        self.front = self.front.next # set the next object of the front node as front node
            
        self.size -= 1 # only cache and separated with node
        
        return pop_node.value

def queue_info(queue):
    print(f"--------------- INFO ---------------")
    print(f"Queue Content: {queue}")
    print(f"Queue Count  : {queue.get_size()}")
    print(f"Queue Empty  : {queue.is_empty()}\n")

# Driver Code
if __name__ == '__main__':
    queue = Queue()
    
    queue_info(queue)
    
    for _ in range(10):
        push = queue.push(randint(1, 9))
        print(f"Push: {push}")
    print()
    
    queue_info(queue)
    
    for _ in range(5):
        pop = queue.pop()
        print(f"Pop: {pop}")
    print()
    
    queue_info(queue)