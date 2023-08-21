# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]
print ("The initial List: ", li)

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is: ", end="")
print(list(li))

# using heappush() to push elements into heap
push_value = int(input("\nEnter one value to push in Heap-tree: "))
heapq.heappush(li, push_value)

# printing modified heap
print("The modified heap after push is: ", end="")
print(list(li))

# using heappop() to pop smallest element
print("\nThe popped and smallest element is: ", end="")
print(heapq.heappop(li))

print("The modified heap after pop is: ", end="")
print(list(li))