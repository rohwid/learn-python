def print_array(a, b, c):
    print(a, b, c)

array = [1, 2, 3]
parse_array = [*array]

print(*array)
print_array(*array)

for i in parse_array:
    print(i)