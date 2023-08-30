from random import randint

class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
	
class Stack:
  def __init__(self):
    self.start = self.head = None
    self.size = 0

  # Pushes element onto stack
  def push(self, value):
    node = Node(value) # instantiate new node
    
    print(f"Push: {value}")
    self.size += 1
    
    if self.start == None:
      self.start = self.head = node
      return
    
    # Iteration step by swapping value
    # 0th  - [head_node]
    # 1st  - [prev_head_node, new_head_node] 
    # 2nd  - [start_node, prev_node, top_node]
    # n-th - [start_node, prev_node, ..., top_node]
    node.prev = self.head 
    self.head.next = node
    self.head = node
  
  # Check if stack is empty
  def is_empty(self):
    if self.start:
      return False
    return True

  # Pops top element from stack
  def pop(self):
    if self.is_empty():
      return
    
    print(f"Pop: {self.head.value}")
    
    self.head = self.head.prev
    
    if self.head != None: self.head.next = None
    if self.head == None: self.start = None
    
    self.size -= 1
  
  # Prints the stack from start node
  def print_stack(self):
    if self.is_empty():
      return 'Stack is Empty.'
    
    curr = self.start
    out = ''
    
    while curr != None:
      out += str(curr.value) + ' '
      curr = curr.next
      
    return out
  
  # Prints the stack from head node
  # def print_stack(self):
  #   if self.is_empty():
  #     return 'Stack is Empty.'
    
  #   curr = self.head
  #   out = ''
    
  #   while curr != None:
  #     out += str(curr.value) + ' '
  #     curr = curr.prev
      
  #   return out
  
  # Get size of the stack with the size variable
  def stack_size(self):
    if self.is_empty():
      return "Stack is empty."
    return self.size
  
  # Get size of the stack with next object
  # def stack_size(self):
  #   if self.is_empty():
  #     return "Stack is empty."
  
    # Start count from head
    # curr = self.start
    # len = 0
    
    # while curr != None:
    #   len += 1
    #   curr = curr.next
    
    # return len
  
  # Get size of the stack with prev object
  # Commented because it's optional
  # def stack_size(self):
  #   if self.is_empty():
  #     return "Stack is empty."
    
    # Start count from head
    # curr = self.head
    # len = 0
    
    # while curr != None:
    #   len += 1
    #   curr = curr.prev
    
    # return len

  # Prints top element of the stack
  def head_element(self):
    if self.is_empty():
      return "Stack is empty."
    else:
      return self.head.value
  
  def start_element(self):
    if self.is_empty():
      return "Stack is empty."
    else:
      return self.start.value

def stack_info(stack):
  print(f"--------------- INFO ---------------")
  print(f"Stack Empty         : {stack.is_empty()}")
  print(f"Stack Content       : {stack.print_stack()}")
  print(f"Stack Count         : {stack.stack_size()}")
  print(f"Stack Start Element : {stack.start_element()}")
  print(f"Stack Top Element   : {stack.head_element()}\n")

if __name__ == "__main__":
  stack = Stack()

  # Push then instantiate new node
  for i in range(10):
    stack.push(randint(1, 9))
  print()
    
  stack_info(stack)

  for i in range(6):
    stack.pop()
  print()

  stack_info(stack)