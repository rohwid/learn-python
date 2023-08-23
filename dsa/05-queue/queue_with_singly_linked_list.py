class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    def count_nodes(self, head):
        current = head # assuming that head != None
        count = 1
        
        while current.next is not None:
            current = current.next
            count += 1
            
        return count
    
    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.front = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp

	# Method to remove an item from queue
    def DeQueue(self):
        if self.isEmpty():
            return
        
        temp = self.front
        self.front = temp.next
        
        if(self.front == None):
            self.rear = None

# Driver Code
if __name__ == '__main__':
    q = Queue()
    
    q.EnQueue(10)
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.EnQueue(20)
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.DeQueue()
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.DeQueue()
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.EnQueue(30)
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.EnQueue(40)
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.EnQueue(50)
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}\n")
    
    q.DeQueue()
    print(f"Queue Front : {str(q.front.data if q.front != None else 'Queue Empty')}")
    print(f"Queue Rear  : {str(q.rear.data if q.rear != None else 'Queue Empty')}")