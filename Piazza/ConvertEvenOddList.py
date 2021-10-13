"""
Question -

Given an list of numbers , convert every odd number to even by adding 1 and convert
 every even number to odd by adding 3.

Input : 1 2 3 4 5

Output : 2 5 4 7 6
"""

# Code -

givenList = [1, 2, 3, 4, 5]
answerList = list()

for iterating in givenList:
    if iterating % 2 == 0:
        iterating = iterating + 3
        answerList.append(iterating)
    else:
        iterating = iterating + 1
        answerList.append(iterating)

print(answerList)

"""
Answer - 

[2, 5, 4, 7, 6]

"""


