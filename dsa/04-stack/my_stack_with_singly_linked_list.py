from random import randint

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
	def __init__(self):
		self.top = None
		self.size = 0

	# String representation of the stack
	def __str__(self):
		cur = self.top
		out = ""

		while cur:
			out += str(cur.value) + " "
			cur = cur.next

		if out:
			return out
		else:
			return "Stack is Empty."

	# Get the current size of the stack
	def get_size(self):
		if not self.size:
			return "Stack is Empty."
		return self.size

	# Check if the stack is empty
	def is_empty(self):
		return self.size == 0

	# Push a value into the next stack
	# as an object.
	def push(self, value):
		push_node = Node(value)
		self.size += 1
		
		if self.top == None:
			self.top = push_node
			return
        
		push_node.next = self.top # set the previous top node as the next object of the push_node
		self.top = push_node # set the push_node as the current top node

	# Remove a value from the stack 
	# and return.
	def pop(self):
		if self.is_empty():
			return

		pop_node = self.top
		self.top = self.top.next
  
		self.size -= 1
		
		return pop_node.value

def stack_info(stack):
    print(f"--------------- INFO ---------------")
    print(f"Stack Empty   : {stack.is_empty()}")
    print(f"Stack Content : {stack}")
    print(f"Stack Count   : {stack.get_size()}\n")

# Driver Code
if __name__ == "__main__":
    stack = Stack()
    
    stack_info(stack)
    
    for _ in range(10):
        push = stack.push(randint(1, 9))
        print(f"Push: {push}")
    print()
    
    stack_info(stack)
    
    for _ in range(5):
        pop = stack.pop()
        print(f"Pop: {pop}")
    print()
    
    stack_info(stack)