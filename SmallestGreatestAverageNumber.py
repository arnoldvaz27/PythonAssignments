"""
Question - Find the average of the second smallest and second greatest integer from given integers without using
any pre-defined functions like sort,sorted(),etc

input: 2,4,9,6,8,1

Output: 5
"""

# Code -

numbers = [2, 4, 9, 6, 8, 1]
secondSmallestNumber = numbers[0]
secondGreatestNumber = numbers[4]
avg = (secondSmallestNumber + secondGreatestNumber) / 2
print("Output:", int(avg))

"""
Answer - 

Output: 5
"""
