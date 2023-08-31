class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def is_empty(self):
        return self.front == None
    
    def count_nodes(self):
        if self.is_empty():
            return 'Queue Empty'
        
        current = self.front
        count = 1
        
        while current.next is not None:
            current = current.next
            count += 1
            
        return count
    
    # Method to add an item to the queue
    def enqueue(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.front = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp

	# Method to remove an item from queue
    def dequeue(self):
        if self.is_empty():
            return
        
        temp = self.front
        self.front = temp.next
        
        if(self.front == None):
            self.rear = None

# Driver Code
if __name__ == '__main__':
    q = Queue()
    
    q.enqueue(10)
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")

    
    q.enqueue(20)
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")
    
    q.dequeue()
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")
    
    q.dequeue()
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")

    q.enqueue(30)
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")

    
    q.enqueue(40)
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")
    
    q.enqueue(50)
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}\n")
    
    q.dequeue()
    print(f"Number of Queue : {q.count_nodes()}")
    print(f"Queue Rear      : {q.rear.data if q.rear else 'Queue Empty'}")
    print(f"Queue Front     : {q.front.data if q.front else 'Queue Empty'}")