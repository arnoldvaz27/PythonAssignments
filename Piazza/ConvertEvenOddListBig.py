"""
Question -

Given a lost of numbers , convert every odd integer into even by adding 1 and convert every even integer into odd by adding 3.
input : 2 3 4 1 8 11
output : 5 4 7 2 11 12
explanation : odd places numbers are added by 1 and even number are added by 3.

"""

# Code -

givenList = [2, 3, 4, 1, 8, 11]
answerList = list()

for iterating in givenList:
    if iterating % 2 == 0:
        iterating = iterating + 3
        answerList.append(iterating)
    else:
        iterating = iterating + 1
        answerList.append(iterating)

print(answerList)

