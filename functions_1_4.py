def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        if num>2 and num==0:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    return list(filter(is_prime, numbers))
x = input()
numbers = list(map(int, x.split()))
my_fav_primes = filter_prime(numbers)
print(my_fav_primes)