# Function to rotate string left and right by d length

# Code -


def rotate(inputs, d):
    # slice string in two parts for left and right
    Lfirst = inputs[0: d]
    Lsecond = inputs[d:]
    Rfirst = inputs[0: len(inputs) - d]
    Rsecond = inputs[len(inputs) - d:]

    # now concatenate two parts together
    print("Left Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))


inputs = 'perfectplanb'
d = 2
rotate(inputs, d)

"""
Answer - 

Left Rotation :  rfectplanbpe
Right Rotation :  nbperfectpla

"""