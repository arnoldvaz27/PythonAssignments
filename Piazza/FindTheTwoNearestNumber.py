"""
Question -

find the two nearest numbers from a given list of numbers

input : 1,3,7,8

output : 7,8

.

input : 1,9,2,5

output : 1,2

"""

# Code -

givenList = [1, 9, 2, 5]
outputList = list()
for iterating in givenList:
    for iteratingSecond in givenList:
        number = int(iterating)
        number += 1
        if number == iteratingSecond:
            outputList.append(iterating)
            outputList.append(iteratingSecond)

print(outputList)

"""
Answer 

[1, 2]

"""