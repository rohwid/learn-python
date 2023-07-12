def search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
print(arr1)

print(f"9 in \"arr1\" were on index {search(arr1, 11)}")
print(f"3 in \"arr1\" were on index {search(arr1, 3)}\n")

arr2 = [3]
print(arr2)

print(f"6 in \"arr2\" were on index {search(arr2, 6)}")
print(f"3 in \"arr2\" were on index {search(arr2, 3)}\n")

arr3 = [6, 3, 10, 7, 8, 1, 11, 13]
arr3.sort()
print(arr3)

print(f"1 in \"arr3\" were on index {search(arr3, 1)}")
print(f"3 in \"arr3\" were on index {search(arr3, 3)}")