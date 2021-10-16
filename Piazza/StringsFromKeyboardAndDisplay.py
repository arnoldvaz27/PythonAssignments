"""
Question -

Write a program that reads a string from keyboard and display:

The number of uppercase letters in the string
The number of lowercase letters in the string
The number of digits in the string
The number of whitespace characters in the string
Input: Stay home during the COVID-19 outbreak.

Output: The number of uppercase letters: 6

The number of lowercase letters: 24

The number of digits: 2

The number of whitespace characters: 5

remaining - week 9/19 to 9/25 ( 9/22/21 and 9/19/21)

"""

# Code -

InputString = input("Enter string: ")
Upper = 0
Lower = 0
Digit = 0
WhiteSpace = 0


def checkWhiteSpace(StringAlpha):
    if StringAlpha == " ":
        return StringAlpha
    else:
        return 0


for iterating in InputString:
    if iterating.isupper():
        Upper = Upper + 1
    elif iterating.islower():
        Lower = Lower + 1
    elif iterating.isdigit():
        Digit = Digit + 1
    elif checkWhiteSpace(iterating):
        resultReturn = checkWhiteSpace(iterating)
        if resultReturn != 0:
            WhiteSpace = WhiteSpace + 1

print("The number of uppercase letters:", Upper)
print("The number of lowercase letters:", Lower)
print("The number of digits:", Digit)
print("The number of whitespace characters:", WhiteSpace)

"""
Answer -

Enter string: Stay home during the COVID-19 outbreak.
The number of uppercase letters: 6
The number of lowercase letters: 24
The number of digits: 2
The number of whitespace characters: 5

"""