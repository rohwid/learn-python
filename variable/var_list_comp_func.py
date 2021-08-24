def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled_comp = [double(x) for x in sequence]
doubled_map = map(double, sequence)

print(sequence)
print(doubled_comp)
print(list(doubled_map))