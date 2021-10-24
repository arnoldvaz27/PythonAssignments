"""
Question -

Given a two Python list. Iterate both lists simultaneously such
that list1 should display item in original order and list2 in
reverse order

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200
40 100

a = [0, 1, 2, 3]
for a[0] in a:
    print(a[0])

"""

# Code -

# @title
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)
