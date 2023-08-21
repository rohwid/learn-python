class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    # String representation of the stack
    def __str__(self):
        cur = self.head
        out = ""
        
        while cur:
            out += str(cur.value) + " "
            cur = cur.next # change to next node
            
        if out:
            return out
        else:
            return "Queue is Empty."
    
    # Method to add an item to the queue
    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        
        if self.head == None:
            self.head = self.tail = new_node
            return
        
        # Iteration step
        # 0th  - [head]
        # 1st  - [head, new_node] 
        # 2nd  - [head, tail, new_node]
        # n-th - [head, previous_tail, ..., tail, new_node]
        self.tail.next = new_node # add new node as next tail node
        self.tail = new_node # set new node as tail node

	# Method to remove an item from queue
    def dequeue(self):
        if self.is_empty():
            return
        
        # Iteration step
        # n-th - [delete_node <- previous_tail, previous_tail, ..., previous_tail]
        # final length n = start length n - number loop range
        pop_node = self.head
        self.head = self.head.next
            
        self.size -= 1
        
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
    
    for i in range(10):
        queue.enqueue(i + 1)
    
    queue_info(queue)
    
    for _ in range(5):
        remove = queue.dequeue()
        print(f"Pop: {remove}")
    
    print()
    queue_info(queue)