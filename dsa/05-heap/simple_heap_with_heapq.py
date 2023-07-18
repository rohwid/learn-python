
# importing "heapq" to implement heap queue
import heapq
 
# initializing list
li = [5, 7, 9, 1, 3]
print ("The initial List: ", li)


# using heapify to convert list into heap
heapq.heapify(li)
 
# printing created heap
print ("The created heap from List is: ", (list(li)))