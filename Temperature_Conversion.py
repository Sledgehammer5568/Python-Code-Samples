# Emanuel Ramos
#
# 10/19/2022
#
# Description: this program converts Fahrenheit into Celsius
#

# The user needs to input the integer related to the Fahrenheit they want to convert.
F = int(input("what temp is it in Fahrenheit?\n"))

# This is the equation to convert Fahrenheit into Celsius.
C = (F - 32) * 5 / 9

# The program will print the Fahrenheit given by the user.
print("The current temp in Fahrenheit:", F)

# The program will input the calculated conversion from Fahrenheit to Celsius.
print("The current temp in Celsius is:", C)
