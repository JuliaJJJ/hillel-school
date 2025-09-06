import random

length = random.randint(3, 10)

arr = []
i = 0
while i < length:
    num = random.getrandbits(32)
    arr.append(num)
    i += 1

finish_arr = []

finish_arr.append(arr[0])
finish_arr.append(arr[2])
finish_arr.append(arr[-2])

print("arr:", arr)
print("finish_arr:", finish_arr)
