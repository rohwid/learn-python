class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
	
class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  # Pushes element onto stack
  def push(self, element):
    node = Node(element) # instantiate new node
    
    self.size += 1
    
    if self.head == None:
      self.head = node
      return
    
    # Iteration step by swapping value
    # 0th  - [start_node/top_node]
    # 1st  - [start_node, top_node] 
    # 2nd  - [start_node, prev_node, top_node]
    # n-th - [start_node, prev_node, ..., top_node]
    node.prev = self.head 
    self.head.next = node
    self.head = node
  
  # Check if stack is empty
  def is_empty(self):
    if self.head:
      return False
    return True

  # Pops top element from stack
  def pop(self):
    if self.is_empty():
      print('Stack is Empty')
      return
    
    print(f"Pop: {self.head.value}")
    
    self.head = self.head.prev
    
    if self.head != None: self.head.next = None
    
    self.size -= 1
  
  # Get size of the stack with the size variable
  def stack_size(self):
    if self.is_empty():
      return "Stack is empty."
    return self.size
  
  # Prints the stack
  def print_stack(self):
    if self.is_empty():
      return 'Stack is Empty.'
    
    curr = self.head
    out = ''
    
    while curr != None:
      out += str(curr.value) + ' '
      curr = curr.prev
      
    return out

  # Prints top element of the stack
  def head_element(self):
    if self.is_empty():
      return "Stack is empty."
    else:
      return self.head.value

  # Get size of the stack from prev object
  # def stack_size(self):
  #   if self.is_empty():
  #     return "Stack is empty."
    
  #   curr = self.head
  #   len = 0
    
  #   while curr != None:
  #     len += 1
  #     curr = curr.prev
    
  #   return len

def stack_info(stack):
  print(f"--------------- INFO ---------------")
  print(f"Stack Empty       : {stack.is_empty()}")
  print(f"Stack Content     : {stack.print_stack()}")
  print(f"Stack Count       : {stack.stack_size()}")
  print(f"Stack Top Element : {stack.head_element()}\n")

if __name__ == "__main__":
  stack = Stack()

  # Push then instantiate new node
  for i in range(10):
    stack.push(i + 1)
    
  stack_info(stack)

  for i in range(7):
    stack.pop()
  print()

  stack_info(stack)