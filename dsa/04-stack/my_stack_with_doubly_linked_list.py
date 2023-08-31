from random import randint

class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
	
class Stack:
  def __init__(self):
    self.start = self.top = None
    self.size = 0

  # Pushes element onto stack
  def push(self, value):
    push_node = Node(value) # instantiate new node
    
    self.size += 1
    
    if self.start == None:
      self.start = self.top = push_node
      return
    
    push_node.prev = self.top # set previous top node as the previous object of the push_node
    self.top.next = push_node # set push_node as the next object of previous top node
    self.top = push_node # set push_node as the current top node
    
    return push_node.value
  
  # Check if stack is empty
  def is_empty(self):
    if self.start:
      return False
    return True

  # Pops top element from stack
  def pop(self):
    if self.is_empty():
      return
    
    pop_node = self.top # pop the top node
    self.top = self.top.prev # set the top node to the previous node
    
    # set next node to none
    if self.top: self.top.next = None

    # reset start node
    if not self.top: self.start = None
    
    self.size -= 1
    
    return pop_node.value
  
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
  
  # Prints the stack from top node
  # def print_stack(self):
  #   if self.is_empty():
  #     return 'Stack is Empty.'
    
  #   curr = self.top
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
  
    # Start count from start node
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
    
    # Start count from top
    # curr = self.top
    # len = 0
    
    # while curr != None:
    #   len += 1
    #   curr = curr.prev
    
    # return len

  # Prints top element of the stack
  def top_element(self):
    if self.is_empty():
      return "Stack is empty."
    else:
      return self.top.value
  
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