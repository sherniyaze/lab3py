def histogram(numberslist):
    for x in numberslist:
        print("*" * x)


my_list = []
x = int(input())
for _ in range(x):
    num = int(input())
    my_list.append(num)
histogram(my_list)

