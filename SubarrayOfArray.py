"""
Question -

#write a program to print all subarrays of an array

"""

# Code -

numbers = [1, 2, 3, 4]
sublists = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        sublists.append(numbers[i:j])
print(sublists)

"""
Answer - 

[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

"""
