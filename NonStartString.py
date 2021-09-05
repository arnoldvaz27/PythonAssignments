"""
Question -
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'

non_start('java', 'code') → 'avaode'

non_start('shotl', 'java') → 'hotlava'
"""


# Code -

def non_start(first_string, second_string):
    print(first_string[1:] + second_string[1:])


non_start('Hello', 'There')
non_start('java', 'code')
non_start('shotl', 'java')


"""
Answer - 

non_start('Hello', 'There') -> ellohere
non_start('java', 'code') -> avaode
non_start('shotl', 'java') -> hotlava

"""
