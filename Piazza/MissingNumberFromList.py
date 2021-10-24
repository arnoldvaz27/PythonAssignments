"""
Question -

Write a python function to print the missing number from a list.

Example:

Input: [1, 2, 3, 4, 6, 7, 8, 9]

Output: 5

"""

# Code -

givenList = [1, 2, 3, 4, 6, 7, 8, 9]
for iterating in range(givenList[0], givenList[-1]):
    if iterating not in givenList:
        print(iterating)

"""
Answer -

5

"""
