"""
Question -

#how to create a Numpy array filled with all one, given the shape and type of array.

output -
        Matrix a :
                [1 1 1]

        Matrix b :
                [[1 1 1]
                [1 1 1]
                [1 1 1]]
"""

# Code -

import numpy as np

a = np.ones(3)
print("Matrix a :\n", np.round(a.transpose()).astype(int))
b = np.ones((3, 3))
print("Matrix b :\n", np.round(b.transpose()).astype(int))

"""
Answer - 

Matrix a :
 [1 1 1]
Matrix b :
 [[1 1 1]
 [1 1 1]
 [1 1 1]]

"""
