arr = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

zeros = []
others = []

i = 0
while i < len(arr):
    if arr[i] == 0:
        zeros.append(arr[i])
    else:
        others.append(arr[i])
    i += 1

arr = others + zeros

print(arr)
