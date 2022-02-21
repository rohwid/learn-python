def print_struct(a, b, c):
    print(a, b, c)

struct = {'a': 10, 'b':20, 'c': 30}

print_struct(**struct)
