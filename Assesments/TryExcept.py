hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    floatingHours = float(hours)
    floatingRate = float(rate)
except:
    print("Error, please enter numeric input")
