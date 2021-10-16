"""
Question -

Python Program to Check if a Number is a Palindrome or not.

INPUT:151

OUTPUT:The number is a palindrome!


"""


# Code -

def palindrome(givenstring):
    reversedstring = []
    concatestring = ""
    for b in givenstring[::-1]:
        reversedstring.append(b)
    concatestring = concatestring.join(reversedstring)
    if concatestring == givenstring:
        print("The number is a Palindrome")
    else:
        print("The number is not Palindrome")


palindrome('151')
