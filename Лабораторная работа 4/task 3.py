def delete(list1, index=None):
    if index is None:
        list1 = list1[:-1]
    else:
        list1 = list1[:index] + list1[index +1:]
    return list1


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
