list_of_nums = []
n = int(input())
i = 0
for x in range(n):
    num = int(input())
    for x in range(n):
        if num != list_of_nums[i] and i == n-1:
            list_of_nums.append(num)
        elif num != list_of_nums[i] and i != n-1:
            continue
        else:
            continue

    

print(list_of_nums)