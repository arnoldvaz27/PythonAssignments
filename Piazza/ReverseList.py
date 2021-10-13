"""
Question -

Reverse a list without using reverse() function

Example:

INPUT: [1, 2, 3, 4, 5]

OUTPUT: [5, 4, 3, 2, 1]


"""

# Code -

givenList = [1, 2, 3, 4, 5]
reversedList = list()
for iterating in givenList[::-1]:
    reversedList.append(iterating)

print(reversedList)

"""
Answer - 

[5, 4, 3, 2, 1]

"""
