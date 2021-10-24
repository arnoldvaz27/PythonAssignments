"""
Question -

Given a number, we need to find sum of its digits using recursion.

Examples:

Input : 321

Output :6

.

Input : 9876543210

Output : 45

"""


# Code -

def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(int(n / 10))


# Driven code to check above
num = 9876543210
result = sum_of_digit(num)
print("Sum of digits in", num, "is", result)


"""
Answer -

Sum of digits in 9876543210 is 45

"""