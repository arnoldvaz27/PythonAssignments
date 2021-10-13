"""
Question :

Given a List of Numbers, you are required to find the second maximum number?

Note - List Contains duplicate numbers

Example: Input : [0,2,8,5,4,6,3,5,7,8,7] Output : 7
"""

# Code -

given_List = [0, 2, 8, 5, 4, 6, 3, 5, 7, 8, 7]
given_List.sort()
lastElementOfSortedList = given_List[-1]
secondMaximumNumber = 0
for b in given_List[::-1]:
    if b < lastElementOfSortedList:
        secondMaximumNumber = b
        break

print("Output: ", secondMaximumNumber)

# Answer

# Output:  7
