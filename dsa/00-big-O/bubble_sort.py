# Big-O = O(n^2)
def bubble_sort(arr):
  n = len(arr)
  
  for i in range(n):
    for j in range(0, (n - i) - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
  return arr

arr = [0, 6, 7, 9, 4, 2, 4, 1]

print(f"Input  : {arr}")
print(f"Output : {bubble_sort(arr)}")