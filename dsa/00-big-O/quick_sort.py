# Big-O = O(n * log(n))
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[len(arr) // 2]
  
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  
  return quick_sort(left) + middle + quick_sort(right)

arr = [0, 6, 7, 9, 4, 2, 4, 1]

print(f"Input  : {arr}")
print(f"Output : {quick_sort(arr)}")