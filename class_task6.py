x = int(input())
my_numbers = []
for _ in range(x):
    num = int(input())
    my_numbers.append(num)
filtred_nums = list(filter(lambda x: x>1 and all(x% i != 0 for i in range(2,int(x**0.5)+1)), my_numbers))
print(filtred_nums)
