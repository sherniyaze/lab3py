def setlist(list_k):
    list_1 = []
    for num in list_k:
        if num not in list_1:
            list_1.append(num)
    return list_1

size = int(input())
list_k = []
for x in range(size):
    nums = int(input())
    list_k.append(nums)
print(setlist(list_k))