a = []
b = a
c = []
d = 1234
e = "hello"

a.append(35)

print(id(a))
print(id(b))
print(id(c))

# integer are imutable
d = 5678

print(id(d))

tup = ('physics', 'chemistry', 1997, 2000)
print("Print tuple1 element-0: ", tup[0])

## Following action is not valid for tuples
## It means tuple are imutable
# tup1[0] = 100;

d += 1
e += " world"

print(d)
print(id(d))
print(e)
print(id(e))