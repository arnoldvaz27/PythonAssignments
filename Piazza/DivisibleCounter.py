"""
Question -

take an input as list of numbers , and print all the numbers that are divisible by 10

input : 1 3 20 25 30 output : 2 explanation : 20,30 are both divisbile 10 ,
you need to return output as 2


"""

# Code -

givenList = [1, 3, 20, 25, 30]
counter = 0
for iterating in givenList:
    if iterating % 10 == 0:
        counter = counter + 1

print(counter)

"""
Answer - 

2
"""
