list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

## Access value in list 1
print("Print all list: ", list1)
print("Print list element-0: ", list1[0])
print("Print list element-1: ", list1[1])
print("Print list element-1 until 3: ", list1[1:3])
print("Print list element-1 until 4: ",list1[1:4])
print("Print list element-2 until end: ",list1[2:])
print("Print list twice: ",tinylist * 2)
print("Join two list: ", list1 + tinylist, "\n")

list2 = ['physics', 'chemistry', 1997, 2000]

## Access value in list 2
print("Print all list: ", list2)
print("Print list element-0: ", list2[0])
print("Print list element-1 until 5: ", list2[1:5], "\n")

## Updating list
print("Value available at index 2: ", list2[2])
list2[2] = 2001
print("New value available at index 2: ", list2[2], "\n")

## Delete list
print("Before deleting value at index 2 : ", list2)
del list2[2]
print ("After deleting value at index 2 : ", list2)

## Try matrices
mat1 = [[1,2,3],[4,5,6]]
print("Matices1: ", mat1)
print("Print matrices in row 0: ", mat1[0])
print("Print matrices in row 0 col 2: ", mat1[0][2])
