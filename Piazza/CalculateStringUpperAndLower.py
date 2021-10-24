"""
Question -

Write a Python function that accepts a string and calculate the
number of upper case letters and lower case letters

INPUT:'The quick Brow Fox'

OUTPUT:

No. of Upper case characters : 3

No. of Lower case Characters : 12

"""

# Code -

givenString = 'The quick Brow Fox'
Upper = 0
Lower = 0

for iterating in givenString:
    if iterating.isupper():
        Upper = Upper + 1
    elif iterating.islower():
        Lower = Lower + 1

print("No. of Upper case characters :", Upper)
print("No. of Lower case Characters :", Lower)


"""
Answer - 

No. of Upper case characters : 3
No. of Lower case Characters : 12

"""