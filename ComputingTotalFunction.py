"""
def computeTotalpay(days, rate):
    return float(days * rate)


print(computeTotalpay(45, 10))
"""


def computeTotalpay(days, rate):
    return float(days * rate)


Days = input("Enter hours: ")
Rate = input("Enter rate: ")
try:
    floatingHours = float(Days)
    floatingRate = float(Rate)
    print(computeTotalpay(floatingHours, floatingRate))
except:
    print("Error, please enter numeric input")
