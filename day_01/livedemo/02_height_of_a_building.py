# Program to estimate the height of a building

import math

# input
d = float(input("Enter distance from building: "))
a = float(input("Angle in degrees: "))

# process
h = d * math.tan(math.radians(a))

# output
print("---------------------------------------")
print("Height of the building: ", h, " mts")
