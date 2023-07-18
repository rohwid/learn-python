import heapq

# Initialize a list with some values
values = [5, 1, 3, 7, 4, 2]
print ("The initial List is: ", values)

# Convert the list into a heap
heapq.heapify(values)
print("The created Heap is: ", values)

# Add a new value to the heap
push_value = int(input("\nEnter one value to push in Heap-tree: "))
heapq.heappush(values, push_value)
print("Heap after push:", values)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(values)

# Print the smallest element and the updated heap
print("\nSmallest element:", smallest)
print("Heap after pop:", values)

# Get the n smallest elements from the heap
n_smallest = heapq.nsmallest(3, values)
print("\nSmallest 3 elements:", n_smallest)

# Get the n largest elements from the heap
n_largest = heapq.nlargest(3, values)
print("Largest 3 elements:", n_largest)