a = []
b = a
c = []
d = 1234
e = "hello"

# list are muteable
print(f'val a : {a}')
print(f'id a  : {id(a)}')

a.append(35)

print(f'val a : {a}')
print(f'id a  : {id(a)}')

print(f'val b : {b}')
print(f'id b  : {id(b)}')

# ------------------

print(f'id c  : {id(c)}')

# integer are imutable

print(f'id d  : {id(d)}')

# string are imutable

print(f'val e : {e}')
print(f'id e  : {id(e)}')

d = 5678

print(f'id d  : {id(d)}')

# -------------------

tup = ('physics', 'chemistry', 1997, 2000)
print(f'Print tuple1 element - 0 : {tup[0]}')

## Following action is not valid for tuples
## It means tuple are imutable
# tup[0] = 100;

# -------------------

# string and integer are imutable

d += 1
e += " world"

print(f'val d : {d}')
print(f'id d  : {id(d)}')
print(f'val e : {e}')
print(f'id e  : {id(e)}')