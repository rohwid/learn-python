from random import randint

class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
	
class Stack:
  def __init__(self):
    self.start = self.top = None
    
  # Check if stack is empty
  def is_empty(self):
    if self.start:
      return False
    return True

  # Pushes element onto stack
  def push(self, value):
    push_node = Node(value) # instantiate new node
    
    if self.start == None:
      self.start = self.top = push_node
      return
    
    # Swapping value
    push_node.prev = self.top
    self.top.next = push_node
    self.top = push_node
    
    return push_node.value

  # Determines the size of the stack
  def stack_size(self):
    if self.is_empty():
      return "Stack is empty."
    
    curr = self.start
    len = 0
    
    while curr != None:
      len += 1
      curr = curr.next
    
    return len

  # Pops top element from stack
  def pop(self):
    if self.is_empty():
      return
    
    pop_node = self.top.value
    self.top = self.top.prev
    
    if self.top != None: self.top.next = None
    if self.top == None: self.start = None
    
    return pop_node

  # Prints the stack
  def print_stack(self):
    if self.is_empty():
      return 'Stack is Empty.'
    
    curr = self.start
    out = ''
    
    while curr != None:
      out += str(curr.value) + ' '
      curr = curr.next
      
    return out
  
  # Prints top element of the stack
  def start_element(self):
    if self.is_empty():
      return "Stack is empty."
    else:
      return self.start.value

  # Prints top element of the stack
  def top_element(self):
    if not self.top:
      return "Stack is empty."
    else:
      return self.top.value
  
def stack_info(stack):
  print(f"--------------- INFO ---------------")
  print(f"Stack Empty         : {stack.is_empty()}")
  print(f"Stack Content       : {stack.print_stack()}")
  print(f"Stack Count         : {stack.stack_size()}")
  print(f"Stack Start Element : {stack.start_element()}")
  print(f"Stack Top Element   : {stack.top_element()}\n")


if __name__ == "__main__":
  stack = Stack()

  # Push then instantiate new node
  for i in range(10):
    push = stack.push(randint(1, 9))
    print(f"Push: {push}")
  print()
    
  stack_info(stack)

  for i in range(6):
    pop = stack.pop()
    print(f"Pop: {pop}")
  print()

  stack_info(stack)
