"""
Question -

Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1

count_hi('ABChi hi') → 2

count_hi('hihi') → 2

"""


# Code -

def count_hi(string):
    counter = 0
    for i in range(len(string)):
        if string[i] == "h" and string[i + 1] == "i":
            counter = counter + 1
            continue

    return counter


print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))


"""
Answer - 

1
2
2

Output Matched - 

count_hi('abc hi ho') → 1

count_hi('ABChi hi') → 2

count_hi('hihi') → 2

"""