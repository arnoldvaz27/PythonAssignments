"""
Question 1 :
Create a file named "file.txt" with the following text mentioned below.
You are requested to extract Day i.e. Sat, Sun etc from this file and
print the days so that your output looks like: SatSunMonTueWed.
(Print the output in new lines i.e. Sat then next line Sun then next line Mon etc.)
"""

# Code :

fhand = open('email.txt', 'r')
for iterating in fhand:
    weekdays = iterating.rstrip().split()
    print(weekdays[2])
