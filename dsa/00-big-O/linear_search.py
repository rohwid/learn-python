# Big-O = O(n)
def linear_search(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return -1

arr = [0, 6, 7, 9, 4, 2, 4, 1]
print(f"Found at index number {linear_search(arr, 9)}.")