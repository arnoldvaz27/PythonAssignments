"""
Question -

Write a Python program to sort a list alphabetically in a dictionary.

Demo code -

#@title
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)

"""

# Code -

dictionary = {
    'n1': [2, 3, 1],
    'n2': [5, 1, 2],
    'n3': [3, 2, 4]
}

print("\nBefore Sorting: ")
for x in dictionary.items():
    print(x)

print("\nAfter Sorting: ")

for i, j in dictionary.items():
    sorted_dict = {i: sorted(j)}
    print(sorted_dict)

# Answer -

"""

Before Sorting: 
('n1', [2, 3, 1])
('n2', [5, 1, 2])
('n3', [3, 2, 4])

After Sorting: 
{'n1': [1, 2, 3]}
{'n2': [1, 2, 5]}
{'n3': [2, 3, 4]}

"""