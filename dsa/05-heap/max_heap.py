# function to swap two numbers
def swapping(x, y):
    t = y
    y = x
    x = t
    
    return x, y

# function to insert a value into the heap tree
def insert_heap_tree(ht, val):
    tree_size = len(ht)
    
    if tree_size == 0:
        ht.append(val)
    else:
        ht.append(val)
        i = tree_size
        
        while i != 0 and ht[i] > ht[(i - 1) // 2]:
            x, y = swapping(ht[i], ht[(i - 1) // 2])
            ht[i] = x
            ht[(i - 1) // 2] = y
            i = (i - 1) // 2

# function to delete a value from the heap tree
def delete_value(ht, val):
    tree_size = len(ht)
    i = 0
    
    for i in range(tree_size):
        if val == ht[i]:
            break
    
    x, y = swapping(ht[i], ht[tree_size - 1])
    ht[i] = x
    ht[tree_size - 1] = y
    ht.pop()

# function to print the heap tree
def print_array(ht):
	
	for i in range(len(ht)):
		print(ht[i], end=" ")
	print()

heap_tree = []
del_value = 0

insert_heap_tree(heap_tree, 3)
print(f'Root: {heap_tree}')

insert_heap_tree(heap_tree, 4)
print(f'Tree: {heap_tree}')

insert_heap_tree(heap_tree, 9)
print(f'Tree: {heap_tree}')

insert_heap_tree(heap_tree, 5)
print(f'Tree: {heap_tree}')

insert_heap_tree(heap_tree, 12)
print(f'Tree: {heap_tree}')

insert_heap_tree(heap_tree, 7)
print(f'Tree: {heap_tree}')

insert_heap_tree(heap_tree, 15)
print(f'Tree: {heap_tree}')

insert_heap_tree(heap_tree, 20)
print(f'Tree: {heap_tree}')

print("\nHEAP DATA STRUCTURE - INSERT & DELETE OPERATION")
print("Inserted Values in Heap-Tree")
print_array(heap_tree)

del_value = int(input("\nEnter one value from above Heap-tree values - to delete in Heap-tree: "))
delete_value(heap_tree, del_value)
print("After deleting an element: ", end="")
print_array(heap_tree)
