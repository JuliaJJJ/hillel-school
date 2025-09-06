arr = [12, 3, 4, 10, 8]
arr_finish = []

if len(arr) > 0:
    last_el = arr[-1]
    arr_finish = [last_el]

    i = 0
    while i < len(arr) - 1:
        arr_finish.append(arr[i])
        i += 1

print(arr_finish)