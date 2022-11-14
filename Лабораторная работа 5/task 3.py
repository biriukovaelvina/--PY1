from random import randint
def get_unique_list_numbers(left, right, num) -> list[int]:
    list_1 = []
    while len(list_1)<num and num<=len(range(left, right))+1:
        s=randint(left, right)
        if s not in list_1:
            list_1.append(s)
    return list_1
print(get_unique_list_numbers(-10, 10, 15))
