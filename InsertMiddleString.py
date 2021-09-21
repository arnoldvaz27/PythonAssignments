"""
Question -

Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.

input---

s1 = "Ault" s2 = "Kelly"

output---
AuKellylt

"""


# Code -

def appendMiddle(s1, s2):
    middleIndex = int(len(s1) / 2)
    print("Original Strings are", s1, s2)
    middleThree = s1[:middleIndex:] + s2 + s1[middleIndex:]
    print("After appending new string in middle", middleThree)


appendMiddle("Ault", "Kelly")


"""
Answer - 

Original Strings are Ault Kelly
After appending new string in middle AuKellylt

"""
