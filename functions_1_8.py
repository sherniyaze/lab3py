def spy_game(nums):
    spy = [0,0,7]
    for i in nums:
        if i == spy[0]:
            spy.pop(0)
        if not spy:
            return True
    return False

numbers = input()
numbers = list(map(int, numbers.split()))
spy = spy_game(numbers)
print(spy)