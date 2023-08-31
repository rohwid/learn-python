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
		self.head = Node("head")
		self.size = 0

	# String representation of the stack
	def __str__(self):
		curr = self.head.next
		out = ""

		while curr:
			out += str(curr.value) + " "
			curr = curr.next

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

	# Get the top item of the stack
	def peek(self):

		# Sanitary check to see if we
		# are peeking an empty stack.
		if self.is_empty():
			raise Exception("Peeking from an empty stack")
		return self.head.next.value

	# Push a value into the next stack
	# as an object.
	def push(self, value):
		push_node = Node(value)
		push_node.next = self.head.next
		self.head.next = push_node
		
		self.size += 1

		return push_node.value

	# Remove a value from the stack 
	# and return.
	def pop(self):
		if self.is_empty():
			raise Exception("Popping from an empty stack")

		pop_node = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return pop_node.value

def stack_info(stack):
    print(f"--------------- INFO ---------------")
    print(f"Stack Content: {stack}")
    print(f"Stack Count  : {stack.get_size()}")
    print(f"Stack Empty  : {stack.is_empty()}\n")

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