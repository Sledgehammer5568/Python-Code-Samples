# Emanuel Ramos
#
# 10/19/2022
#
# Description: this program calculates MPG
#

# The program requires the user to input the amount of miles driven.
M = int(input("how many miles have you driven?\n"))

# The program also requires the user to input how many gallons were used by driving.
G = int(input("how many gallons of gas have you used?\n"))

# This is the equation needed to figure out how many miles per gallon are used.
MPG = M / G

# The program will print out the miles and gallons inputted.
print("Miles driven:", M)
print("Gallon used:", G)

# This prints out the answer according to the Miles and Gallons inputted.
print("This is how many miles you get per gallon of gas: ", MPG)
