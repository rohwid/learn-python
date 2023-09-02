# Big-O = O(log(n))
def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  
  while low <= high:
    mid = (low + high) // 2
    print(f"Steps: (low: {low}; mid: {mid}; high: {high})")
    
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      return mid
  
  return -1

arr = [0, 6, 7, 9, 4, 2, 4, 1]
arr.sort() # binary search require sorting

print(f"Input: {arr}")
print(f"Found at index number {binary_search(arr, 2)}.")