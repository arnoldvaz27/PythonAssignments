"""
Question -

Concatenate two lists index-wise

Given: list1 = ["M", "na", "i", "Ke"] list2 = ["y", "me", "s", "lly"]

Output: ['My', 'name', 'is', 'Kelly']

"""

# Code -

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i, j in zip(list1, list2):
    list3.append(i + j)

print(list3)

"""
Answer -

['My', 'name', 'is', 'Kelly']

"""