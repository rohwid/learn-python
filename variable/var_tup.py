tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

## Accessing values in tuples
print("Print all tuple1: ", tup1)
print("Print all tuple2: ", tup2)
print("Print tuple1 element-0: ", tup1[0])
print("Print tuple1 element-1 until 5: ", tup2[1:5])

## Following action is not valid for tuples
## It means tuple are imutable
# tup1[0] = 100;

## Updating tuples
tup3 = (12, 34.56)
tup4 = ('abc', 'xyz')

print("Print all tuple3: ", tup3)
print("Print all tuple4: ", tup4)
tup5 = tup3 + tup4
print("Merge tuple3 and tuple4: ", tup5)

## Delete tuple
tup6 = ('physics', 'chemistry', 1997, 2000)
print("Print all tuple6: ", tup6)

## Following action is not valid for tuples
## It means tuple are imutable
# del tup6[0]
# print("After deleting tuple6 element-0 : ", tup6)

del tup6
print("After deleting all tuple6 : ")
print(tup6)