class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
	def __init__(self):
		self.head = None
		self.size = 0

	# String representation of the stack
	def __str__(self):
		cur = self.head
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
		return self.size

	# Check if the stack is empty
	def is_empty(self):
		return self.size == 0

	# Push a value into the next stack
	# as an object.
	def push(self, value):
		new_node = Node(value)
		self.size += 1
		
		if self.head == None:
			self.head = new_node
			return
        
        # Iteration step by swapping value
        # 0th  - [head]
        # 1st  - [new_node, next_head] 
        # 2nd  - [new_node, next_head, next_head]
        # n-th - [new_node, next_head, ..., next_head]
		new_node.next = self.head # initiate the next node
		self.head = new_node # append new node

	# Remove a value from the stack 
	# and return.
	def pop(self):
		if self.is_empty():
			return

		# Iteration step
        # n-th - [delete_node <- next_head, next_head, ..., next_head]
        # final length n = start length n - number loop range
		remove = self.head
		self.head = self.head.next
  
		self.size -= 1
		
		return remove.value

def stack_info(stack):
    print(f"--------------- INFO ---------------")
    print(f"Stack Empty   : {stack.is_empty()}")
    print(f"Stack Content : {stack}")
    print(f"Stack Count   : {stack.get_size()}\n")

# Driver Code
if __name__ == "__main__":
    stack = Stack()
    
    stack_info(stack)
    
    for i in range(10):
        stack.push(i + 1)
    
    stack_info(stack)
    
    for _ in range(5):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print()
    
    stack_info(stack)