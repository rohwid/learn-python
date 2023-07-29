# A complete working Python program to
# demonstrate all stack operations using
# a doubly linked list
class node:
  def __init__(self,val):
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

  # pushes element onto stack
  def push(self,element):
    newP = node(element)
    
    if self.start == None:
      self.start = self.top = newP
      return
    
    newP.prev = self.top
    self.top.next = newP
    self.top = newP

  # Determines the size of the stack
  def stacksize(self):
    curr = self.start
    len = 0
    
    while curr != None:
      len += 1
      curr = curr.next
    
    print("Size of the stack is : ", len)

  # Pops top element from stack
  def pop(self):
    if self.isEmpty():
      print('List is Empty')
      return
    
    self.top = self.top.prev
    
    if self.top != None: self.top.next = None

  # Prints the stack
  def printstack(self):
    if self.isEmpty():
      print('List is Empty')
      return
    
    curr = self.start
    print("Stack is : ", end='')
    
    while curr != None:
      print(curr.val, end = ' ')
      curr = curr.next
    print()

  # Prints top element of the stack
  def topelement(self):
    if self.isEmpty():
      print("Stack is empty")
    else:
      print("The element at top of the stack is : ",self.top.val)


stack = Stack()
stack.push(2)
stack.push(5)
stack.push(10)
stack.printstack()
stack.topelement()
stack.stacksize()
stack.pop()
print("Element popped from the stack ")
stack.topelement()
stack.pop()
print("Element popped from the stack")
stack.stacksize()
