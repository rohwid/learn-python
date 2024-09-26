sets = {1, 2, 3, 4, 5}
print(f'current sets: {sets}')

sets.add(6)
print(f'after add 6: {sets}')

sets.add(5)
print(f'after add 5: {sets}')

sets.remove(6)
print(f'after remove 6: {sets}')

sets.discard(6)
print(f'after discard 6: {sets}')

sets.discard(5)
print(f'after discard 5: {sets}')

sets.clear()
print(f'after clear: {sets}')