# Python code to demonstrate working of
# nlargest() and nsmallest()
 
# importing "heapq" to implement heap queue
import heapq
 
# initializing list
li = [6, 7, 9, 4, 3, 5, 8, 10, 1]
print ("The initial List: ", li)
 
# using heapify() to convert list into heap
heapq.heapify(li)

print("The created heap is: ", end="")
print(list(li))

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are: ", end="")
print(heapq.nlargest(3, li))
 
# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are: ", end="")
print(heapq.nsmallest(3, li))