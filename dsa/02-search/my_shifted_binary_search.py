def search(arr, target):
    left = 0
    right = len(arr) - 1
        
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

def shift(arr, target_idx):
    if target_idx >= 0:
        left = arr[(target_idx) + 1:]
        right = arr[:(target_idx) + 1]
        
        return left + right
    else:
        return arr

arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
print(arr1)

print(f"9 in arr1: [-2, 3, 4, 7, 8, 9, 11, 13] were on index {search(arr1, 9)}")
print(f"arr1: [-2, 3, 4, 7, 8, 9, 11, 13] shifted by 9 into arr1: {shift(arr1, search(arr1, 9))}")
print(f"3 in arr1: [-2, 3, 4, 7, 8, 9, 11, 13] were on index {search(arr1, 3)}")
print(f"arr1: [-2, 3, 4, 7, 8, 9, 11, 13] shifted by 3 into arr1: {shift(arr1, search(arr1, 3))}\n")

arr2 = [3]
print(arr2)

print(f"6 in arr2: [3] were on index {search(arr2, 6)}")
print(f"arr2: [3] shifted by 6 into arr2: {shift(arr2, search(arr1, 6))}")
print(f"3 in arr2: [3] were on index {search(arr2, 3)}")
print(f"arr2: [3] shifted by 3 into arr2: {shift(arr2, search(arr1, 3))}\n")