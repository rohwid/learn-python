# A complete working Python program to
# demonstrate all stack operations using
# a doubly linked list
class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None
	
class Stack:
  def __init__(self):
    self.start = self.top = None
    
  # Check if stack is empty
  def isEmpty(self):
    if self.start:
      return False
    
    return True

  # Pushes element onto stack
  def push(self, element):
    node = Node(element) # instantiate new node
    
    if self.start == None:
      self.start = self.top = node
      return
    
    # Swapping value
    node.prev = self.top
    self.top.next = node
    self.top = node

  # Determines the size of the stack
  def stack_size(self):
    curr = self.start
    len = 0
    
    while curr != None:
      len += 1
      curr = curr.next
    
    print("Size of the stack is : ", len)

  # Pops top element from stack
  def pop(self):
    if self.isEmpty():
      print('Stack is Empty')
      return
    
    self.top = self.top.prev
    
    if self.top != None: self.top.next = None
    
    print("\nOne element popped from the stack.\n")

  # Prints the stack
  def print_stack(self):
    if self.isEmpty():
      print('Stack is Empty.')
      return
    
    curr = self.start
    print("Stack is : ", end='')
    
    while curr != None:
      print(curr.val, end = ' ')
      curr = curr.next
    print()

  # Prints top element of the stack
  def top_element(self):
    if self.isEmpty():
      print("Stack is empty.")
    else:
      print("The element of the top stack is : ", self.top.val)


if __name__ == "__main__":
  stack = Stack()

  # Push then instantiate new node
  stack.push(2)
  stack.push(5)
  stack.push(7)

  stack.print_stack()
  stack.top_element()
  stack.stack_size()

  stack.pop()

  stack.print_stack()
  stack.top_element()
  stack.stack_size()

  stack.pop()
  
  stack.print_stack()
  stack.top_element()
  stack.stack_size()
