# Create 1D list
n_arr_0 = 5
arr_0 = [0] * n_arr_0
print(f"arr_0 {arr_0}")

arr_0[0] = 1
print(f"arr_0 {arr_0}")


# 1D list with list comprehension
n_arr_1 = 5
arr_1 = [0 for i in range(n_arr_1)]
print(f"arr_1 {arr_1}")

arr_1[0] = 1
print(f"arr_1 {arr_1}")


# create 2D list
rows, cols = (3, 4)
arr_2 = [[0]*cols]*rows
print(f"arr_2 {arr_2}")

for i in arr_2:
    print(i)

arr_2[0][0] = 1
print(f"arr_2 {arr_2}")

for i in arr_2:
    print(i)

print(f"row: {len(arr_2)}")
print(f"col: {len(arr_2[0])}")

# 2D list with list comprehension
rows, cols = (3, 4)
arr_3 = [[0 for i in range(cols)] for j in range(rows)]
print(f"arr_3 {arr_3}")

for i in arr_3:
    print(i)

arr_3[0][0] = 1
print(f"arr_3 {arr_3}")

for i in arr_3:
    print(i)

print(f"row: {len(arr_3)}")
print(f"col: {len(arr_3[0])}")

# 2D list with empty list
rows, cols = (4, 6)
arr_4 = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr_4.append(col)
print(f"arr_4 {arr_4}")

for i in arr_4:
    print(i)

arr_4[0][0] = 1
print(f"arr_4 {arr_4}")

for i in arr_4:
    print(i)

print(f"row: {len(arr_4)}")
print(f"col: {len(arr_4[0])}")

mat1 = [[1,2,3],[4,5,6]]
print("Matices1: ", mat1)
print("Print matrices in row 0: ", mat1[0])
print("Print matrices in row 0 col 2: ", mat1[0][2])

for i in mat1:
    for j in i:
        print(j)