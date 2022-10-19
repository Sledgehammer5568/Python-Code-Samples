# Emanuel Ramos
#
# 10/19/2022
#
# Description: A program that tells you what day of the week you will be returning on from vacation
# when the date you left and the number of days you plan on staying are inputted
#

# First we must ask the user to input the day that they left on vacation, and we will give that answer the variable "S".
S = int(input("""What day of the week did you leave on vacation?
0 = sunday
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday\n"""))  # Only the integers displayed here can be inputted.

# This first if statement is meant to rule out any unwanted inputs for the variable "S".
if 0 <= S <= 6:

    # If the first input is correct we must then ask the user to input the number of days they will be on vacation.
    L = int(input("How many days will you go on vacation?\n"))  # Variable "L" is given for "Length" of time.

    # Here we calculate the remainder as "N" with the "L" input.
    N = L % 7  # We are using 7 because there are only 7 days in a week.

    # We make a new variable called "D" to show the sum of "S" and "N", "D" should be the answer if it is <= 6.
    D = S + N
    # Here we define that if D is <= 6 to be a limit, because D is the answer .
    if D <= 6:
        print("You will come back on:", D)  # If the requirement is met "D" will be printed.

    # Here we must define that if "D" goes over 6 we must subtract 7 to make it the correct day.
    elif D > 6:
        print("You will come back on:", D - 7)  # We subtract by 7 because the program doesn't stop adding after Sunday.

# if the user inputs anything other than 0, 1, 2, 3, 4, 5, 6 for "S" the program can't continue, retry.
else:
    print("incorrect input, please try again")
