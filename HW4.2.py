arr = [0, 1, 7, 2, 4, 8]
result = 0
i = 0

while i < len(arr):
    if i == 0 or i % 2 == 0:
        result += arr[i]
    i += 1

result *= arr[-1]

print(result)