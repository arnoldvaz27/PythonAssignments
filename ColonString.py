"""
Question 1 :
Take the following Python code that stores a string:`str =
Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
floating point number.
"""

# Code -

str1 = 'Perfect-Plan-B:0.7541'
strFind = str1.find(':')
print(strFind)
sliced = str1[strFind+1:]
slicedToFloat = float(sliced)
print(slicedToFloat)
print(type(slicedToFloat))


