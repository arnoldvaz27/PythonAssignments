"""
Question -

Given two strings (of lowercase letters), a pattern and a string.
The task is to sort string according to the order defined by pattern
and return the reverse of it. It may be assumed that pattern has all
characters of the string and all characters in pattern appear only once.

Examples:

Input : pat = "asbcklfdmegnot", str = "eksge"

Output : str = "geeks" (after sorting, str becomes "skeeg" and return its reverse)

Input : pat = "mgewqnasibkldjxruohypzcftv", str = "niocgd"

Output : str = "coding"

"""

# Code -

"""
pattern = "asbcklfdmegnot"
givenString = "eksge"
"""
pattern = input("Enter the pattern: ")
checkString = input("Enter the string to check: ")
outputString = ""
outputStringReversed = ""
for iteratePatten in pattern:
    for iterateCheck in checkString:
        if iteratePatten in iterateCheck:
            outputString += iteratePatten

for iterating in outputString[::-1]:
    outputStringReversed += iterating

print("Pattern Fetched -", outputString)
print("Reversed -", outputStringReversed)


"""
Answer -
1) 
Enter the pattern: asbcklfdmegnot
Enter the string to check: eksge
Pattern Fetched - skeeg
Reversed - geeks

2)
Enter the pattern: mgewqnasibkldjxruohypzcftv
Enter the string to check: niocgd
Pattern Fetched - gnidoc
Reversed - coding

"""