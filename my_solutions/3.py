def is_prime(x: int):
    """Returns whether x is prime"""
    
    if x < 2:
        return False
    else:   
        return all(x % i for i in range(2, int(x**0.5)+1))


def is_lucky(x: int):
    """Returns whether x is lucky"""

    sum_digits = sum([int(i) for i in str(x)])
    sum_squared_digits = sum([int(i)**2 for i in str(x)])

    return is_prime(sum_digits) and is_prime(sum_squared_digits)


# Get inputs
inputs = [input() for i in range(int(input()))]

# Calculate and print results
for line in inputs:
    nums = [int(i) for i in line.split()]
    to_test = range(nums[0], nums[1] + 1)
    results = [is_lucky(i) for i in to_test]

    print(results.count(True))
