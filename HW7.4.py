def common_elements():
    range_number = 100

    list1 = [x for x in range(range_number) if x % 3 == 0]
    list2 = [x for x in range(range_number) if x % 5 == 0]
    return set(list1) & set(list2)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

