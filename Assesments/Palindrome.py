"""
Question -

# Given a string, write a python function to check if it is palindrome or not.
A string is said to be palindrome if the reverse of the string is the same as string.
For example, “radar” is a palindrome, but “radix” is not a palindrome.

Input : malayalam
    Output : Yes

    Input : geeks
    Output : No
"""


# Code -

def palindrome(givenstring):
    reversedstring = []
    concatestring = ""
    for b in givenstring[::-1]:
        reversedstring.append(b)
    concatestring = concatestring.join(reversedstring)
    if concatestring == givenstring:
        print(givenstring+" is a Palindrome")
    else:
        print(givenstring+" is Not Palindrome")


palindrome('malayalam')
palindrome('geeks')


"""
Answer - 

malayalam is a Palindrome
geeks is Not Palindrome

"""


# Code 2 -

"""

def palindrome(givenstring):
    reversedstring = []
    concatestring = ""
    for b in givenstring[::-1]:
        reversedstring.append(b)
    concatestring = concatestring.join(reversedstring)
    if concatestring == givenstring:
        print("Yes")
    else:
        print("No")


palindrome('malayalam')
palindrome('geeks')


Answer - 

Yes
No


"""
