"""
Question -

Write a Python program to append a new item to the end of the array.
   Sample Output:
   Original array: array('i', [1, 3, 5, 7, 9])
   Append 11 at the end of the array:
   New array: array('i', [1, 3, 5, 7, 9, 11])

"""

# Code -

givenArray = ('i', [1, 3, 5, 7, 9])

print("Original Array", givenArray)
for iterating in givenArray:
    if type(iterating) == list:
        var = iterating
        var.append(11)

print("\nNew Array", givenArray)

"""
Answer -

Original Array ('i', [1, 3, 5, 7, 9])

New Array ('i', [1, 3, 5, 7, 9, 11])

"""