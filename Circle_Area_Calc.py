# Emanuel Ramos
#
# 10/19/2022
#
# Description: this program calculates the area of a circle when given the radius
#

# The program requires the input of the "radius" of the circle, so it can run.
r = int(input("what is the radius of the circle?\n"))

# pi is a constant so it is classified.
pi = 3.14

# This is the equation on how to get the area of a circle given the "Area".
A = pi * r ** 2

# The radius inputted will be displayed as well as the area that the program calculated.
print("This is the radius:", r)
print("This is the area of the circle:", A)
