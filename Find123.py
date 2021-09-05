"""
Question: -

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True

array123([1, 1, 2, 4, 1]) → False

array123([1, 1, 2, 1, 2, 3]) → True
"""


# Code :

def array123(array):
    for i in range(len(array)):
        if (i + 2) <= len(array):
            if array[i] == 1 and (array[i + 1] == 2) and (array[i + 2] == 3):
                return True
            continue
        else:
            return False

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))

"""
Answer - 
print(array123([1, 1, 2, 3, 1])) → True
print(array123([1, 1, 2, 4, 1])) → False
print(array123([1, 1, 2, 1, 2, 3])) → True
"""
