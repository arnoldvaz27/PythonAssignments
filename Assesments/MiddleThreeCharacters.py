"""
Question -

Get middle three characters function

input : "JhonDipPeta"

output : Dip
"""


def getMiddleThreeChars(sampleStr):
    middleIndex = int(len(sampleStr) / 2)
    print("Original String is", sampleStr)
    middleThree = sampleStr[middleIndex - 1:middleIndex + 2]
    print("Middle three chars are", middleThree)


getMiddleThreeChars("ArnoldVaz")
