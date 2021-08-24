sequence = [1, 3, 5, 9]
doubled_comp = [(lambda x: x * 2)(x) for x in sequence]
doubled_map = map(lambda x: x * 2, sequence)

print(sequence)
print(doubled_comp)
print(list(doubled_map))