# Andre Tonkovidov
# atonkovi@ucsc.edu
# pa1
# Calculates volume and surface area of a sphere with a user-defined radius.

r = float(input("Enter the radius of the sphere:"))
from math import pi as p
SA = 4*p*r**2
V = (4/3)*p*r**3
print("The volume is:", V)
print("The surface area is:", SA)