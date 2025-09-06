arr = [1, 2, 3, 4, 5, 6]
arr1 = []
arr2 = []

center_arr_index = round(len(arr) / 2)

i = 0
while i < len(arr):
    if i < center_arr_index:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])
    i += 1

finish_arr = [arr1, arr2]
print(finish_arr)
